import logging

from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ControlSurface import ControlSurface
from _Framework.DeviceComponent import DeviceComponent
from _Framework.InputControlElement import MIDI_NOTE_TYPE
from _Framework.Layer import Layer
from _Framework.MixerComponent import MixerComponent
from _Framework.Resource import SharedResource
from _Framework.TransportComponent import TransportComponent
from .components import Encoder, MidiValues, Slider


class G25(ControlSurface):
    def __init__(self, *a, **k):
        ControlSurface.__init__(self, *a, **k)

        self._logger = logging.getLogger('Graphite_25')

        self._set_suppress_rebuild_requests(True)
        with self.component_guard():
            self._common_channel = 0
            self._shift_button = ButtonElement(True, MIDI_NOTE_TYPE, self._common_channel, MidiValues.RECORD,
                                               resource_type=SharedResource, name='Shift_Button')  # RECORD button
            self._init_transport_component()
            self._init_mixer_component()
            self._init_device_component()
        self._set_suppress_rebuild_requests(False)

    def handle_sysex(self, midi_bytes):
        if len(midi_bytes) == 7 and midi_bytes[0] == 0xF0 and midi_bytes[6] == 0xF7:
            if midi_bytes[1:5] == (127, 127, 4, 1):
                if self._mixer:  # todo: use correct condition
                    self.song().master_track.mixer_device.volume.value = midi_bytes[5] / 128.0
        else:
            self._logger.error('unknown sysex: ' + str(midi_bytes))

    def _init_device_component(self):
        self._device = DeviceComponent(device_selection_follows_track_selection=True, name='Device_Component')

        layer_specs = {}

        parameter_encoders_raw = [
            Encoder(self._common_channel, 0, name='Device_Parameter_0_Control'),  # E1
            Encoder(self._common_channel, 1, name='Device_Parameter_1_Control'),  # E2
            Encoder(self._common_channel, 2, name='Device_Parameter_2_Control'),  # E3
            Encoder(self._common_channel, 3, name='Device_Parameter_3_Control'),  # E4
            Encoder(self._common_channel, 4, name='Device_Parameter_4_Control'),  # E5
            Encoder(self._common_channel, 5, name='Device_Parameter_5_Control'),  # E6
            Encoder(self._common_channel, 6, name='Device_Parameter_6_Control'),  # E7
            Encoder(self._common_channel, 7, name='Device_Parameter_7_Control')  # E8
        ]
        layer_specs['parameter_controls'] = ButtonMatrixElement(rows=[parameter_encoders_raw])

        self._device.layer = Layer(**layer_specs)

        self.set_device_component(self._device)

    def _init_mixer_component(self):
        # self._master_volume_control = Slider()

        self._mixer = MixerComponent(16, 2)
        # self._mixer.master_strip().set_volume_control(self._master_volume_control)

        self._next_track_button = ButtonElement(True, MIDI_NOTE_TYPE, self._common_channel, MidiValues.FFWD)
        self._prev_track_button = ButtonElement(True, MIDI_NOTE_TYPE, self._common_channel, MidiValues.RWD)
        self._mixer.set_select_buttons(self._next_track_button, self._prev_track_button)

    def _init_transport_component(self):
        def make_transport_button(note_id, name):
            return ButtonElement(True, MIDI_NOTE_TYPE, self._common_channel, note_id, name=name)

        layer_specs = {'stop_button': make_transport_button(MidiValues.STOP, 'Stop_Button'),
                       'play_button': make_transport_button(MidiValues.PLAY, 'Play_Button'),
                       # used as Shift button 'record_button': make_transport_button(114, 'Record_Button'),
                       # used as Prev Track or Prev Device (with Shift) 'seek_backward_button': make_transport_button(116, 'Rwd_Button'),
                       # used as Next Track or Next Device (with Shift) 'seek_forward_button': make_transport_button(117, 'FFwd_Button')
                       }
        self._transport = TransportComponent(name='Transport')
        self._transport.layer = Layer(**layer_specs)
