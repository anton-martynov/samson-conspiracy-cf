from _Framework.ControlSurface import ControlSurface
from _Framework.TransportComponent import TransportComponent
from _Framework.MixerComponent import MixerComponent
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.Resource import PrioritizedResource
from .Controls import TransportButton, XFader, Slider, LaunchScenePad, LaunchClipPad, NavButton

import logging

logger = logging.getLogger('ConspiracySurface')


class Conspiracy(ControlSurface):
    """ Script for Samson's Conspiracy Controller """

    def __init__(self, *a, **k):
        super(Conspiracy, self).__init__(*a, **k)

        self._session_width = 4
        self._session_height = 5

        with self.component_guard():
            self._create_controls()
            self._create_session()
            self._create_transport()
            self._create_mixer()

            self._session.set_mixer(self._mixer)
            self.set_highlighting_session_component(self._session)

        logger.info('Surface initialized')

    def _create_controls(self):
        self._shift_button = TransportButton(self, 40, resource_type=PrioritizedResource, name='Shift_Button')
        self._left_button = NavButton(34, name='Bank_Select_Left_Button')
        self._right_button = NavButton(36, name='Bank_Select_Right_Button')
        self._up_button = NavButton(35, name='Bank_Select_Up_Button')
        self._down_button = NavButton(37, name='Bank_Select_Down_Button')

        self._scene_launch_buttons = [
            LaunchScenePad(4, name='Scene_0_Launch_Button'),
            LaunchScenePad(9, name='Scene_1_Launch_Button'),
            LaunchScenePad(14, name='Scene_2_Launch_Button'),
            LaunchScenePad(19, name='Scene_3_Launch_Button'),
            LaunchScenePad(24, name='Scene_4_Launch_Button')
        ]
        self._scene_launch_buttons = ButtonMatrixElement(name='Scene_Launch_Buttons', rows=[self._scene_launch_buttons])

        self._matrix = ButtonMatrixElement(name='Button_Matrix')
        for scene_index in xrange(self._session_height):
            row = [
                LaunchClipPad(scene_index * 5 + track_index, name='%d_Clip_%d_Button' % (track_index, scene_index)) for track_index in xrange(self._session_width)
            ]
            self._matrix.add_row(row)

    def _create_session(self):
        self._session = SessionComponent(self._session_width, self._session_height, name='Session_Control', auto_name=True, enable_skinning=True)
        self._session.set_clip_launch_buttons(self._matrix)
        self._session.set_scene_launch_buttons(self._scene_launch_buttons)

        self._session.set_track_bank_left_button(self._left_button)
        self._session.set_track_bank_right_button(self._right_button)
        self._session.set_scene_bank_up_button(self._up_button)
        self._session.set_scene_bank_down_button(self._down_button)

        for scene_index in xrange(self._session_height):
            scene = self._session.scene(scene_index)
            for track_index in xrange(self._session_width):
                clip_slot = scene.clip_slot(track_index)
                clip_slot.name = '%d_Clip_Slot_%d' % (track_index, scene_index)

        logger.info('Session created')

    def _create_transport(self):
        self._transport = TransportComponent()
        self._transport.set_play_button(TransportButton(self, 38))
        self._transport.set_stop_button(TransportButton(self, 39, False))
        # self._transport.set_record_button(TransportButton(self, 40))

        logger.info('Transport elements created')

    def _create_mixer(self):
        self._mixer = MixerComponent(4, 2)  # 4 tracks, 2 returns
        self._mixer.master_strip().set_volume_control(XFader(name='Master_Volume_Control'))

        # tracks volume & pan
        self._mixer.channel_strip(0).set_volume_control(Slider(30))
        self._mixer.channel_strip(1).set_volume_control(Slider(31))
        self._mixer.channel_strip(2).set_volume_control(Slider(32))
        self._mixer.channel_strip(3).set_volume_control(Slider(33))
        self._mixer.channel_strip(0).set_pan_control(Slider(26))
        self._mixer.channel_strip(1).set_pan_control(Slider(27))
        self._mixer.channel_strip(2).set_pan_control(Slider(28))
        self._mixer.channel_strip(3).set_pan_control(Slider(29))

        # return tracks volume
        self._mixer.return_strip(0).set_volume_control(Slider(24))
        self._mixer.return_strip(1).set_volume_control(Slider(25))

        logger.info('Mixer elements created')
