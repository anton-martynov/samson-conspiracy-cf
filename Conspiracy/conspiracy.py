import logging

from _APC.DetailViewCntrlComponent import DetailViewCntrlComponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ControlSurface import ControlSurface
from _Framework.DeviceComponent import DeviceComponent
from _Framework.Layer import Layer
from _Framework.MixerComponent import MixerComponent
from _Framework.Resource import PrioritizedResource
from _Framework.SessionComponent import SessionComponent
from _Framework.TransportComponent import TransportComponent
from .controls import TransportButton, XFader, Slider, LaunchScenePad, LaunchClipPad, NavButton, FButton, Encoder, DeviceFButton

logger = logging.getLogger('ConspiracySurface')


class Conspiracy(ControlSurface):
    """ Script for Samson's Conspiracy Controller """

    SESSION_WIDTH = 4
    SESSION_HEIGHT = 5

    def __init__(self, *a, **k):
        super(Conspiracy, self).__init__(*a, **k)

        self._suggested_input_port = self._suggested_output_port = 'Conspiracy'

        with self.component_guard():
            self._create_controls()
            self._create_session()
            self._create_transport()
            self._create_mixer()
            self._create_device_component()
            self._create_detail_view_control()

            self._session.set_mixer(self._mixer)
            self.set_device_component(self._device)
            self.set_highlighting_session_component(self._session)

        logger.info('Surface initialized')

    def _create_real_controls(self):
        # transport section
        self._play_button = TransportButton(38)
        self._stop_button = TransportButton(39, False)
        self._shift_button = TransportButton(40, False, resource_type=PrioritizedResource)  # 40 - Record

        # navigation
        self._left_button = NavButton(34)
        self._right_button = NavButton(36)
        self._up_button = NavButton(35)
        self._down_button = NavButton(37)

        # encoders, E1 .. E8
        self._parameter_knobs = [
            Encoder(16 + i % (i + 1)) for i in xrange(8)
        ]

        # F1 - F4, tracks select
        self._select_buttons = [
            FButton(25 + i % (i + 1)) for i in xrange(self.SESSION_WIDTH)
        ]

        # F5 - F8
        self._button_f5 = DeviceFButton(29)
        self._button_f6 = DeviceFButton(30)
        self._button_f7 = DeviceFButton(31)
        self._button_f8 = DeviceFButton(32)

        # F9, F10
        # self._button_f9 = FButton(33)
        self._button_f10 = FButton(41)

        # 5 / 25 pads, right column
        self._scene_launch_buttons = [
            LaunchScenePad(4),
            LaunchScenePad(9),
            LaunchScenePad(14),
            LaunchScenePad(19),
            LaunchScenePad(24)
        ]

        # 20 / 25 pads
        self._matrix_buttons = [ [ LaunchClipPad(scene * 5 + track) for track in xrange(self.SESSION_WIDTH) ] for scene in xrange(self.SESSION_HEIGHT) ]

        # sliders S1 .. S6
        self._sliders = [
            Slider(26),
            Slider(27),
            Slider(28),
            Slider(29),
            Slider(24),
            Slider(25)
        ]

        self._crossfader_control = XFader()
        self._prehear_volume_control = Encoder(35)

    def _created_shifted_controls(self):
        pass

    def _create_controls(self):
        self._create_real_controls()
        self._created_shifted_controls()

        self._matrix_select_buttons = ButtonMatrixElement(rows=[self._select_buttons])
        self._scene_launch_buttons = ButtonMatrixElement(rows=[self._scene_launch_buttons])
        self._session_matrix = ButtonMatrixElement(rows=self._matrix_buttons)

        logger.info('Controls created')

    def _create_session(self):
        self._session = SessionComponent(self.SESSION_WIDTH, self.SESSION_HEIGHT, auto_name=True, enable_skinning=True, is_enabled=False)
        self._session.set_clip_launch_buttons(self._session_matrix)
        self._session.set_scene_launch_buttons(self._scene_launch_buttons)
        self._session.set_track_bank_left_button(self._left_button)
        self._session.set_track_bank_right_button(self._right_button)
        self._session.set_scene_bank_up_button(self._up_button)
        self._session.set_scene_bank_down_button(self._down_button)
        self._session.set_enabled(True)

        logger.info('SessionComponent created')

    def _create_transport(self):
        self._transport = TransportComponent()
        self._transport.set_play_button(self._play_button)
        self._transport.set_stop_button(self._stop_button)

        logger.info('Transport created')

    def _create_mixer(self):
        self._mixer = MixerComponent(4, auto_name=True, is_enabled=False)
        self._mixer.master_strip().set_volume_control(self._sliders[5])  # Slider 6
        self._mixer.master_strip().set_select_button(self._button_f10)

        # tracks volume
        self._mixer.channel_strip(0).set_volume_control(self._sliders[0])  # Slider 1
        self._mixer.channel_strip(1).set_volume_control(self._sliders[1])  # Slider 2
        self._mixer.channel_strip(2).set_volume_control(self._sliders[2])  # Slider 3
        self._mixer.channel_strip(3).set_volume_control(self._sliders[3])  # Slider 4

        self._mixer.set_track_select_buttons(self._matrix_select_buttons)
        self._mixer.set_crossfader_control(self._crossfader_control)
        self._mixer.set_prehear_volume_control(self._prehear_volume_control)

        self._mixer.set_enabled(True)

        logger.info('MixerComponent created')

    def _create_device_component(self):
        self._device = DeviceComponent(is_enabled=False, device_selection_follows_track_selection=True)
        self._device.set_parameter_controls(tuple(self._parameter_knobs))
        self._device.set_bank_nav_buttons(self._button_f7, self._button_f8)
        self._device.set_enabled(True)

        logger.info('DeviceComponent created')

    def _create_detail_view_control(self):
        self._detail_view_toggler = DetailViewCntrlComponent(is_enabled=False, layer=Layer(device_nav_left_button=self._button_f5, device_nav_right_button=self._button_f6))
        self._detail_view_toggler.set_enabled(True)

        logger.info('DetailViewCntrl created')
