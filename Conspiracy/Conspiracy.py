from _Framework.ControlSurface import ControlSurface
from _Framework.TransportComponent import TransportComponent
from _Framework.MixerComponent import MixerComponent
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from .Controls import TransportButton, XFader, Slider, LaunchScenePad, LaunchClipPad

import logging

logger = logging.getLogger('ConspiracySurface')


class Conspiracy(ControlSurface):
    """ Script for Samson's Conspiracy Controller """

    def __init__(self, *a, **k):
        super(Conspiracy, self).__init__(*a, **k)

        with self.component_guard():
            self._create_session()
            self._create_transport()
            self._create_mixer()

        logger.info('Surface initialized')

    def _create_session(self):
        session_width = 4
        session_height = 5

        self._scene_launch_buttons = [
            LaunchScenePad(4, name='Scene_0_Launch_Button'),
            LaunchScenePad(9, name='Scene_1_Launch_Button'),
            LaunchScenePad(14, name='Scene_2_Launch_Button'),
            LaunchScenePad(19, name='Scene_3_Launch_Button'),
            LaunchScenePad(24, name='Scene_4_Launch_Button')
        ]
        self._scene_launch_buttons = ButtonMatrixElement(name='Scene_Launch_Buttons', rows=[self._scene_launch_buttons])

        self._matrix = ButtonMatrixElement(name='Button_Matrix')
        for scene_index in xrange(session_height):
            row = [
                LaunchClipPad(scene_index * 5 + track_index, name='%d_Clip_%d_Button' % (track_index, scene_index)) for track_index in xrange(session_width)
            ]
            self._matrix.add_row(row)

        self._session = SessionComponent(session_width, session_height, name='Session_Control', auto_name=True)
        self._session.set_clip_launch_buttons(self._matrix)
        self._session.set_scene_launch_buttons(self._scene_launch_buttons)

        for scene_index in xrange(session_height):
            scene = self._session.scene(scene_index)
            for track_index in xrange(session_width):
                clip_slot = scene.clip_slot(track_index)
                clip_slot.name = '%d_Clip_Slot_%d' % (track_index, scene_index)

        logger.info('Session created')

    def _create_transport(self):
        self._transport = TransportComponent()
        self._transport.set_play_button(TransportButton(self, 38))
        self._transport.set_stop_button(TransportButton(self, 39, False))
        self._transport.set_record_button(TransportButton(self, 40))

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
