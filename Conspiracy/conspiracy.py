import logging

from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ComboElement import ComboElement
from _Framework.ControlSurface import ControlSurface
from _Framework.Layer import Layer
from _Framework.MixerComponent import MixerComponent
from _Framework.ModesComponent import ModesComponent, AddLayerMode
from _Framework.Resource import SharedResource
from _Framework.SessionComponent import SessionComponent
from _Framework.TransportComponent import TransportComponent

from .controls import TransportButton, XFader, Slider, LaunchScenePad, LaunchClipPad, NavButton, FButton, Encoder, \
    TrackNavigationFButton

logger = logging.getLogger('ConspiracySurface')


class Conspiracy(ControlSurface):
    """ Script for Samson's Conspiracy Controller """

    SESSION_WIDTH = 4
    SESSION_HEIGHT = 5

    def __init__(self, *a, **k):
        super(Conspiracy, self).__init__(*a, **k)

        self._set_suppress_rebuild_requests(True)

        self._suggested_input_port = self._suggested_output_port = 'Conspiracy'

        with self.component_guard():
            self._create_controls()
            self._create_session()
            self._create_transport()
            self._create_mixer()
            self._create_device_component()
            # self._create_encoder_modes()

            self._session.set_mixer(self._mixer)
            self.set_highlighting_session_component(self._session)

        self._set_suppress_rebuild_requests(False)

        logger.info('Surface initialized')

    def _create_controls(self):
        self._shift_button = TransportButton(40, False, resource_type=SharedResource, name='Shift_Button')

        self._left_button = NavButton(34, name='Bank_Select_Left_Button')
        self._right_button = NavButton(36, name='Bank_Select_Right_Button')
        self._up_button = NavButton(35, name='Bank_Select_Up_Button')
        self._down_button = NavButton(37, name='Bank_Select_Down_Button')

        self._parameter_knobs = [
            Encoder(16 + i, name='Parameter_Knob_%d' % (i + 1)) for i in xrange(8)
        ]

        self._select_buttons = [
             FButton(25 + i, name='Track_Select_%d' % (i + 1)) for i in xrange(self.SESSION_WIDTH)
        ]
        self._matrix_select_buttons = ButtonMatrixElement(name='Track_Select_Buttons', rows=[self._select_buttons])

        # self._volume_button = ComboElement(self._select_buttons[0], modifiers=[self._shift_button])
        # self._pan_button = ComboElement(self._select_buttons[1], modifiers=[self._shift_button])
        # self._send_button = ComboElement(self._select_buttons[2], modifiers=[self._shift_button])
        # self._device_button = ComboElement(self._select_buttons[3], modifiers=[self._shift_button])

        # self._prev_track_button = TrackNavigationFButton(33)  # F9
        # self._next_track_button = TrackNavigationFButton(41)  # F10
        self._prev_track_button = ComboElement(self._left_button, modifiers=[self._shift_button])
        self._next_track_button = ComboElement(self._right_button, modifiers=[self._shift_button])

        self._scene_launch_buttons = [
            LaunchScenePad(4, name='Scene_0_Launch_Button'),
            LaunchScenePad(9, name='Scene_1_Launch_Button'),
            LaunchScenePad(14, name='Scene_2_Launch_Button'),
            LaunchScenePad(19, name='Scene_3_Launch_Button'),
            LaunchScenePad(24, name='Scene_4_Launch_Button')
        ]
        self._scene_launch_buttons = ButtonMatrixElement(name='Scene_Launch_Buttons', rows=[self._scene_launch_buttons])

        self._matrix_buttons = [
            [
                LaunchClipPad(scene * 5 + track, name='%d_Clip_%d_Button' % (track, scene)) for track in xrange(self.SESSION_WIDTH) ] for scene in xrange(self.SESSION_HEIGHT)
            ]

        self._session_matrix = ButtonMatrixElement(name='Button_Matrix', rows=self._matrix_buttons)

        logger.info('Controls created')

    def _create_session(self):
        self._session = SessionComponent(self.SESSION_WIDTH, self.SESSION_HEIGHT, name='Session_Control', auto_name=True, enable_skinning=True)
        self._session.set_clip_launch_buttons(self._session_matrix)
        self._session.set_scene_launch_buttons(self._scene_launch_buttons)

        self._session.set_track_bank_left_button(self._left_button)
        self._session.set_track_bank_right_button(self._right_button)
        self._session.set_scene_bank_up_button(self._up_button)
        self._session.set_scene_bank_down_button(self._down_button)

        for scene_index in xrange(self.SESSION_HEIGHT):
            scene = self._session.scene(scene_index)
            for track_index in xrange(self.SESSION_WIDTH):
                clip_slot = scene.clip_slot(track_index)
                clip_slot.name = '%d_Clip_Slot_%d' % (track_index, scene_index)

        logger.info('Session created')

    def _create_transport(self):
        self._transport = TransportComponent()
        self._transport.set_play_button(TransportButton(38))
        self._transport.set_stop_button(TransportButton(39, False))

        logger.info('Transport elements created')

    def _create_mixer(self):
        self._mixer = MixerComponent(16, 2)
        self._mixer.master_strip().set_volume_control(XFader(name='Master_Volume_Control'))

        # tracks volume & pan
        self._mixer.channel_strip(0).set_volume_control(Slider(26))
        self._mixer.channel_strip(1).set_volume_control(Slider(27))
        self._mixer.channel_strip(2).set_volume_control(Slider(28))
        self._mixer.channel_strip(3).set_volume_control(Slider(29))

        # return tracks volume
        self._mixer.return_strip(0).set_volume_control(Slider(24))
        self._mixer.return_strip(1).set_volume_control(Slider(25))

        self._mixer.set_track_select_buttons(self._matrix_select_buttons)
        self._mixer.set_select_buttons(self._next_track_button, self._prev_track_button)

        logger.info('Mixer elements created')

    def _create_device_component(self):
        # self._device =
        pass

    def _create_encoder_modes(self):
        parameter_knobs_matrix = ButtonMatrixElement([self._parameter_knobs])

        self._encoder_modes = ModesComponent(name='Knob Modes')
        self._encoder_modes.add_mode('volume', AddLayerMode(self._mixer, Layer(volume_controls=parameter_knobs_matrix)))
        self._encoder_modes.add_mode('pan', AddLayerMode(self._mixer, Layer(volume_controls=parameter_knobs_matrix)))
        self._encoder_modes.add_mode('send', AddLayerMode(self._mixer, Layer(volume_controls=parameter_knobs_matrix)))
        self._encoder_modes.add_mode('device', AddLayerMode(self._mixer, Layer(volume_controls=parameter_knobs_matrix)))
        self._encoder_modes.selected_mode = 'volume'
        self._encoder_modes.layer = Layer(volume_button=self._volume_button, pan_button=self._pan_button, send_button=self._send_button, device_button=self._device_button)

        return
