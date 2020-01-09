# Embedded file name: /Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts/Conspiracy/conspiracy.py
from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.DeviceComponent import DeviceComponent
from _Framework.MixerComponent import MixerComponent
from _Framework.SliderElement import SliderElement
from _Framework.TransportComponent import TransportComponent
from _Framework.InputControlElement import *
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.SessionComponent import SessionComponent
from _Framework.EncoderElement import *
from Launchpad.ConfigurableButtonElement import ConfigurableButtonElement


class conspiracy(ControlSurface):

    def __init__(self, c_instance):
        global _map_modes
        global active_mode
        super(conspiracy, self).__init__(c_instance)
        with self.component_guard():
            _map_modes = Live.MidiMap.MapMode
            self.current_track_offset = 0
            self.current_scene_offset = 0
            num_tracks = 128
            num_returns = 24
            self.mixer = MixerComponent(num_tracks, num_returns)
            self._mode0()
            active_mode = '_mode1'
            self._set_active_mode()
            self._arm_follow_track_selection()
            self.show_message('Powered by remotify.io')

    def _mode1(self):
        global direction_tempo_control_updown_mode1
        global lv_tempo_control_updown_mode1
        self.show_message('_mode1 is active')
        self.mixer.channel_strip(0).set_volume_control(EncoderElement(MIDI_CC_TYPE, 0, 42, _map_modes.absolute))
        self.mixer.channel_strip(1).set_volume_control(EncoderElement(MIDI_CC_TYPE, 0, 43, _map_modes.absolute))
        self.mixer.channel_strip(2).set_volume_control(EncoderElement(MIDI_CC_TYPE, 0, 44, _map_modes.absolute))
        self.mixer.channel_strip(3).set_volume_control(EncoderElement(MIDI_CC_TYPE, 0, 45, _map_modes.absolute))
        self.mixer.channel_strip(0).set_pan_control(EncoderElement(MIDI_CC_TYPE, 0, 48, _map_modes.absolute))
        self.mixer.channel_strip(1).set_pan_control(EncoderElement(MIDI_CC_TYPE, 0, 49, _map_modes.absolute))
        self.mixer.channel_strip(2).set_pan_control(EncoderElement(MIDI_CC_TYPE, 0, 50, _map_modes.absolute))
        self.mixer.channel_strip(3).set_pan_control(EncoderElement(MIDI_CC_TYPE, 0, 51, _map_modes.absolute))
        arm_specific_0 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 25)
        arm_specific_0.set_on_off_values(21, 20)
        self.mixer.channel_strip(0).set_arm_button(arm_specific_0)
        arm_specific_1 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 26)
        arm_specific_1.set_on_off_values(21, 20)
        self.mixer.channel_strip(1).set_arm_button(arm_specific_1)
        arm_specific_2 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 27)
        arm_specific_2.set_on_off_values(21, 20)
        self.mixer.channel_strip(2).set_arm_button(arm_specific_2)
        arm_specific_3 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 28)
        arm_specific_3.set_on_off_values(21, 20)
        self.mixer.channel_strip(3).set_arm_button(arm_specific_3)
        send0_controls = (EncoderElement(MIDI_CC_TYPE, 0, 56, _map_modes.absolute),
                          EncoderElement(MIDI_CC_TYPE, 0, 60, _map_modes.absolute),
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None)
        self.mixer.channel_strip(0).set_send_controls(tuple(send0_controls))
        send1_controls = (EncoderElement(MIDI_CC_TYPE, 0, 57, _map_modes.absolute),
                          EncoderElement(MIDI_CC_TYPE, 0, 61, _map_modes.absolute),
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None)
        self.mixer.channel_strip(1).set_send_controls(tuple(send1_controls))
        send2_controls = (EncoderElement(MIDI_CC_TYPE, 0, 58, _map_modes.absolute),
                          EncoderElement(MIDI_CC_TYPE, 0, 62, _map_modes.absolute),
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None)
        self.mixer.channel_strip(2).set_send_controls(tuple(send2_controls))
        send3_controls = (EncoderElement(MIDI_CC_TYPE, 0, 59, _map_modes.absolute),
                          EncoderElement(MIDI_CC_TYPE, 0, 63, _map_modes.absolute),
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None)
        self.mixer.channel_strip(3).set_send_controls(tuple(send3_controls))
        num_tracks = 4
        num_scenes = 5
        self._session = SessionComponent(num_tracks, num_scenes)
        track_offset = self.current_track_offset
        scene_offset = self.current_scene_offset
        self._session.set_offsets(track_offset, scene_offset)
        self._session._reassign_scenes()
        self.set_highlighting_session_component(self._session)
        session_buttons = [0,
                           1,
                           2,
                           3,
                           5,
                           6,
                           7,
                           8,
                           10,
                           11,
                           12,
                           13,
                           15,
                           16,
                           17,
                           18,
                           20,
                           21,
                           22,
                           23]
        session_channels = [0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0]
        session_types = [MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE]
        session_is_momentary = [1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1]
        self._pads = [ButtonElement(session_is_momentary[index], session_types[index], session_channels[index],
                                    session_buttons[index]) for index in range(num_tracks * num_scenes)]
        self._grid = ButtonMatrixElement(
            rows=[self._pads[index * num_tracks:index * num_tracks + num_tracks] for index in range(num_scenes)])
        self._session.set_clip_launch_buttons(self._grid)
        stop_all_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 33)
        self._session.set_stop_all_clips_button(stop_all_button)
        stop_track_buttons = [29,
                              30,
                              31,
                              32]
        stop_track_channels = [0,
                               0,
                               0,
                               0]
        stop_track_types = [MIDI_NOTE_TYPE,
                            MIDI_NOTE_TYPE,
                            MIDI_NOTE_TYPE,
                            MIDI_NOTE_TYPE]
        stop_track_is_momentary = [1,
                                   1,
                                   1,
                                   1]
        self._track_stop_buttons = [ConfigurableButtonElement(stop_track_is_momentary[index], stop_track_types[index],
                                                              stop_track_channels[index], stop_track_buttons[index]) for
                                    index in range(num_tracks)]
        self._session.set_stop_track_clip_buttons(tuple(self._track_stop_buttons))
        scene_buttons = [4,
                         9,
                         14,
                         19,
                         24]
        scene_channels = [0,
                          0,
                          0,
                          0,
                          0]
        scene_types = [MIDI_NOTE_TYPE,
                       MIDI_NOTE_TYPE,
                       MIDI_NOTE_TYPE,
                       MIDI_NOTE_TYPE,
                       MIDI_NOTE_TYPE]
        scene_momentarys = [1,
                            1,
                            1,
                            1,
                            1]
        self._scene_launch_buttons = [
            ButtonElement(scene_momentarys[index], scene_types[index], scene_channels[index], scene_buttons[index]) for
            index in range(num_scenes)]
        self._scene_launch_buttons = ButtonMatrixElement(rows=[self._scene_launch_buttons])
        self._session.set_scene_launch_buttons(self._scene_launch_buttons)
        self._session._enable_skinning()
        self._session.set_stop_clip_triggered_value(23)
        self._session.set_stop_clip_value(21)
        for scene_index in range(num_scenes):
            scene = self._session.scene(scene_index)
            scene.set_scene_value(27)
            scene.set_no_scene_value(20)
            scene.set_triggered_value(24)
            for track_index in range(num_tracks):
                clip_slot = scene.clip_slot(track_index)
                clip_slot.set_triggered_to_play_value(22)
                clip_slot.set_triggered_to_record_value(21)
                clip_slot.set_record_button_value(21)
                clip_slot.set_stopped_value(23)
                clip_slot.set_started_value(22)
                clip_slot.set_recording_value(21)

        for index in range(num_tracks):
            stop_track_button = self._session._stop_track_clip_buttons[index]
            stop_track_button.set_on_off_values(26, 20)

        stop_all_button.set_on_off_values(21, 22)
        self.session_left = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 34)
        self.session_left.set_on_off_values(21, 20)
        self._session.set_track_bank_left_button(self.session_left)
        self.session_right = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 36)
        self.session_right.set_on_off_values(21, 20)
        self._session.set_track_bank_right_button(self.session_right)
        self.session_up = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 35)
        self.session_up.set_on_off_values(21, 20)
        self._session.set_scene_bank_up_button(self.session_up)
        self.session_down = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 37)
        self.session_down.set_on_off_values(21, 20)
        self._session.set_scene_bank_down_button(self.session_down)
        self._session._link()
        self._session.set_mixer(self.mixer)
        self.refresh_state()
        self.mode1_2 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 41)
        self.mode1_2.add_value_listener(self._activate_mode2, identify_sender=False)
        self.mode1_2.send_value(24)
        self.transport = TransportComponent()
        self.transport.name = 'Transport'
        stop_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 39)
        stop_button.set_on_off_values(21, 22)
        stop_button.name = 'stop_button'
        self.transport.set_stop_button(stop_button)
        play_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 38)
        play_button.set_on_off_values(1, 2)
        play_button.name = 'play_button'
        self.transport.set_play_button(play_button)
        overdub_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 40)
        overdub_button.set_on_off_values(21, 22)
        overdub_button.name = 'overdub_button'
        self.transport.set_overdub_button(overdub_button)
        lv_tempo_control_updown_mode1 = 0
        direction_tempo_control_updown_mode1 = 'not set'
        self.tempo_control_updown_encoder = EncoderElement(MIDI_CC_TYPE, 0, 52, _map_modes.absolute)
        self.tempo_control_updown_encoder.add_value_listener(self.tempo_control_updown_mode1, identify_sender=False)
        if hasattr(self, 'mode4_1') and self.mode4_1 is not None:
            self.mode4_1.send_value(23)
        return

    def _remove_mode1(self):
        self.mixer.channel_strip(0).set_volume_control(None)
        self.mixer.channel_strip(1).set_volume_control(None)
        self.mixer.channel_strip(2).set_volume_control(None)
        self.mixer.channel_strip(3).set_volume_control(None)
        self.mixer.channel_strip(0).set_pan_control(None)
        self.mixer.channel_strip(1).set_pan_control(None)
        self.mixer.channel_strip(2).set_pan_control(None)
        self.mixer.channel_strip(3).set_pan_control(None)
        self.mixer.channel_strip(0).set_arm_button(None)
        self.mixer.channel_strip(1).set_arm_button(None)
        self.mixer.channel_strip(2).set_arm_button(None)
        self.mixer.channel_strip(3).set_arm_button(None)
        send0_controls = (None, None, None, None, None, None, None, None)
        self.mixer.channel_strip(0).set_send_controls(tuple(send0_controls))
        send1_controls = (None, None, None, None, None, None, None, None)
        self.mixer.channel_strip(1).set_send_controls(tuple(send1_controls))
        send2_controls = (None, None, None, None, None, None, None, None)
        self.mixer.channel_strip(2).set_send_controls(tuple(send2_controls))
        send3_controls = (None, None, None, None, None, None, None, None)
        self.mixer.channel_strip(3).set_send_controls(tuple(send3_controls))
        self._session.set_clip_launch_buttons(None)
        self.set_highlighting_session_component(None)
        self._session.set_mixer(None)
        self._session.set_stop_all_clips_button(None)
        self._track_stop_buttons = None
        self._session.set_stop_track_clip_buttons(None)
        self._scene_launch_buttons = None
        self._session.set_scene_launch_buttons(None)
        self._session.set_track_bank_left_button(None)
        self._session.set_track_bank_right_button(None)
        self._session.set_scene_bank_up_button(None)
        self._session.set_scene_bank_down_button(None)
        self.current_track_offset = self._session._track_offset
        self.current_scene_offset = self._session._scene_offset
        self._session._unlink()
        self._session = None
        self.mode1_2.send_value(0)
        self.mode1_2.remove_value_listener(self._activate_mode2)
        self.mode1_2 = None
        self.tempo_control_updown_encoder.remove_value_listener(self.tempo_control_updown_mode1)
        self.tempo_control_updown_encoder = None
        self.transport.set_stop_button(None)
        self.transport.set_play_button(None)
        self.transport.set_overdub_button(None)
        self.transport.set_tempo_control(None)
        self.transport = None
        if hasattr(self, 'mode4_1') and self.mode4_1 is not None:
            self.mode4_1.send_value(24)
        return

    def _mode2(self):
        global direction_tempo_fine_control_updown_mode2
        global lv_tempo_fine_control_updown_mode2
        self.show_message('_mode2 is active')
        self.mixer.channel_strip(0).set_volume_control(EncoderElement(MIDI_CC_TYPE, 0, 42, _map_modes.absolute))
        self.mixer.channel_strip(2).set_volume_control(EncoderElement(MIDI_CC_TYPE, 0, 44, _map_modes.absolute))
        self.mixer.channel_strip(3).set_volume_control(EncoderElement(MIDI_CC_TYPE, 0, 45, _map_modes.absolute))
        self.mixer.channel_strip(1).set_volume_control(EncoderElement(MIDI_CC_TYPE, 0, 43, _map_modes.absolute))
        self.a_b_assign_specific_0 = ConfigurableButtonElement(0, MIDI_NOTE_TYPE, 0, 29)
        self.mixer.channel_strip(0).set_crossfade_toggle(self.a_b_assign_specific_0)
        self.a_b_assign_specific_0.add_value_listener(self.update_all_ab_select_LEDs, identify_sender=False)
        self.a_b_assign_specific_1 = ConfigurableButtonElement(0, MIDI_NOTE_TYPE, 0, 30)
        self.mixer.channel_strip(1).set_crossfade_toggle(self.a_b_assign_specific_1)
        self.a_b_assign_specific_1.add_value_listener(self.update_all_ab_select_LEDs, identify_sender=False)
        self.a_b_assign_specific_2 = ConfigurableButtonElement(0, MIDI_NOTE_TYPE, 0, 31)
        self.mixer.channel_strip(2).set_crossfade_toggle(self.a_b_assign_specific_2)
        self.a_b_assign_specific_2.add_value_listener(self.update_all_ab_select_LEDs, identify_sender=False)
        self.a_b_assign_specific_3 = ConfigurableButtonElement(0, MIDI_NOTE_TYPE, 0, 32)
        self.mixer.channel_strip(3).set_crossfade_toggle(self.a_b_assign_specific_3)
        self.a_b_assign_specific_3.add_value_listener(self.update_all_ab_select_LEDs, identify_sender=False)
        send0_controls = (None,
                          None,
                          EncoderElement(MIDI_CC_TYPE, 0, 56, _map_modes.absolute),
                          EncoderElement(MIDI_CC_TYPE, 0, 60, _map_modes.absolute),
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None)
        self.mixer.channel_strip(0).set_send_controls(tuple(send0_controls))
        send1_controls = (None,
                          None,
                          EncoderElement(MIDI_CC_TYPE, 0, 57, _map_modes.absolute),
                          EncoderElement(MIDI_CC_TYPE, 0, 61, _map_modes.absolute),
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None)
        self.mixer.channel_strip(1).set_send_controls(tuple(send1_controls))
        send2_controls = (None,
                          None,
                          EncoderElement(MIDI_CC_TYPE, 0, 58, _map_modes.absolute),
                          EncoderElement(MIDI_CC_TYPE, 0, 62, _map_modes.absolute),
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None)
        self.mixer.channel_strip(2).set_send_controls(tuple(send2_controls))
        send3_controls = (None,
                          None,
                          EncoderElement(MIDI_CC_TYPE, 0, 59, _map_modes.absolute),
                          EncoderElement(MIDI_CC_TYPE, 0, 63, _map_modes.absolute),
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None)
        self.mixer.channel_strip(3).set_send_controls(tuple(send3_controls))
        solo_specific_0 = ConfigurableButtonElement(0, MIDI_NOTE_TYPE, 0, 25)
        solo_specific_0.set_on_off_values(22, 24)
        self.mixer.channel_strip(0).set_solo_button(solo_specific_0)
        solo_specific_1 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 26)
        solo_specific_1.set_on_off_values(22, 24)
        self.mixer.channel_strip(1).set_solo_button(solo_specific_1)
        solo_specific_2 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 27)
        solo_specific_2.set_on_off_values(22, 24)
        self.mixer.channel_strip(2).set_solo_button(solo_specific_2)
        solo_specific_3 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 28)
        solo_specific_3.set_on_off_values(22, 24)
        self.mixer.channel_strip(3).set_solo_button(solo_specific_3)
        num_tracks = 5
        num_scenes = 5
        self._session = SessionComponent(num_tracks, num_scenes)
        track_offset = self.current_track_offset
        scene_offset = self.current_scene_offset
        self._session.set_offsets(track_offset, scene_offset)
        self._session._reassign_scenes()
        self.set_highlighting_session_component(self._session)
        session_buttons = [0,
                           1,
                           2,
                           3,
                           4,
                           5,
                           6,
                           7,
                           8,
                           9,
                           10,
                           11,
                           12,
                           13,
                           14,
                           15,
                           16,
                           17,
                           18,
                           19,
                           20,
                           21,
                           22,
                           23,
                           24]
        session_channels = [0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0]
        session_types = [MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE]
        session_is_momentary = [1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1]
        self._pads = [ButtonElement(session_is_momentary[index], session_types[index], session_channels[index],
                                    session_buttons[index]) for index in range(num_tracks * num_scenes)]
        self._grid = ButtonMatrixElement(
            rows=[self._pads[index * num_tracks:index * num_tracks + num_tracks] for index in range(num_scenes)])
        self._session.set_clip_launch_buttons(self._grid)
        self._session._enable_skinning()
        self._session.set_stop_clip_triggered_value(25)
        self._session.set_stop_clip_value(27)
        for scene_index in range(num_scenes):
            scene = self._session.scene(scene_index)
            scene.set_scene_value(27)
            scene.set_no_scene_value(20)
            scene.set_triggered_value(24)
            for track_index in range(num_tracks):
                clip_slot = scene.clip_slot(track_index)
                clip_slot.set_triggered_to_play_value(26)
                clip_slot.set_triggered_to_record_value(21)
                clip_slot.set_record_button_value(21)
                clip_slot.set_stopped_value(23)
                clip_slot.set_started_value(22)
                clip_slot.set_recording_value(21)

        self.session_down = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 37)
        self.session_down.set_on_off_values(21, 20)
        self._session.set_page_down_button(self.session_down)
        self.session_left = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 34)
        self.session_left.set_on_off_values(21, 20)
        self._session.set_page_left_button(self.session_left)
        self.session_right = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 36)
        self.session_right.set_on_off_values(21, 20)
        self._session.set_page_right_button(self.session_right)
        self.session_up = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 35)
        self.session_up.set_on_off_values(21, 20)
        self._session.set_page_up_button(self.session_up)
        self._session._link()
        self._session.set_mixer(self.mixer)
        self.refresh_state()
        self.mode2_3 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 41)
        self.mode2_3.add_value_listener(self._activate_mode3, identify_sender=False)
        self.mode2_3.send_value(21)
        self.transport = TransportComponent()
        self.transport.name = 'Transport'
        lv_tempo_fine_control_updown_mode2 = 0
        direction_tempo_fine_control_updown_mode2 = 'not set'
        self.tempo_fine_control_updown_encoder = EncoderElement(MIDI_CC_TYPE, 0, 52, _map_modes.absolute)
        self.tempo_fine_control_updown_encoder.add_value_listener(self.tempo_fine_control_updown_mode2,
                                                                  identify_sender=False)
        stop_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 39)
        stop_button.set_on_off_values(21, 20)
        stop_button.name = 'stop_button'
        self.transport.set_stop_button(stop_button)
        play_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 38)
        play_button.set_on_off_values(1, 2)
        play_button.name = 'play_button'
        self.transport.set_play_button(play_button)
        record_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 40)
        record_button.set_on_off_values(1, 2)
        record_button.name = 'record_button'
        self.transport.set_record_button(record_button)
        if hasattr(self, 'mode1_2') and self.mode1_2 is not None:
            self.mode1_2.send_value(21)
        return

    def _remove_mode2(self):
        self.a_b_assign_specific_0.remove_value_listener(self.update_all_ab_select_LEDs)
        self.a_b_assign_specific_1.remove_value_listener(self.update_all_ab_select_LEDs)
        self.a_b_assign_specific_2.remove_value_listener(self.update_all_ab_select_LEDs)
        self.a_b_assign_specific_3.remove_value_listener(self.update_all_ab_select_LEDs)
        self.mixer.channel_strip(0).set_volume_control(None)
        self.mixer.channel_strip(2).set_volume_control(None)
        self.mixer.channel_strip(3).set_volume_control(None)
        self.mixer.channel_strip(1).set_volume_control(None)
        self.mixer.channel_strip(0).set_crossfade_toggle(None)
        self.mixer.channel_strip(1).set_crossfade_toggle(None)
        self.mixer.channel_strip(2).set_crossfade_toggle(None)
        self.mixer.channel_strip(3).set_crossfade_toggle(None)
        send0_controls = (None, None, None, None, None, None, None, None)
        self.mixer.channel_strip(0).set_send_controls(tuple(send0_controls))
        send1_controls = (None, None, None, None, None, None, None, None)
        self.mixer.channel_strip(1).set_send_controls(tuple(send1_controls))
        send2_controls = (None, None, None, None, None, None, None, None)
        self.mixer.channel_strip(2).set_send_controls(tuple(send2_controls))
        send3_controls = (None, None, None, None, None, None, None, None)
        self.mixer.channel_strip(3).set_send_controls(tuple(send3_controls))
        self.mixer.channel_strip(0).set_solo_button(None)
        self.mixer.channel_strip(1).set_solo_button(None)
        self.mixer.channel_strip(2).set_solo_button(None)
        self.mixer.channel_strip(3).set_solo_button(None)
        self.set_highlighting_session_component(None)
        self._session.set_clip_launch_buttons(None)
        self._session.set_mixer(None)
        self._session.set_page_down_button(None)
        self._session.set_page_left_button(None)
        self._session.set_page_right_button(None)
        self._session.set_page_up_button(None)
        self.current_track_offset = self._session._track_offset
        self.current_scene_offset = self._session._scene_offset
        self._session._unlink()
        self._session = None
        self.mode2_3.send_value(0)
        self.mode2_3.remove_value_listener(self._activate_mode3)
        self.mode2_3 = None
        self.tempo_fine_control_updown_encoder.remove_value_listener(self.tempo_fine_control_updown_mode2)
        self.tempo_fine_control_updown_encoder = None
        self.transport.set_stop_button(None)
        self.transport.set_play_button(None)
        self.transport.set_record_button(None)
        self.transport.set_tempo_fine_control(None)
        self.transport = None
        if hasattr(self, 'mode1_2') and self.mode1_2 is not None:
            self.mode1_2.send_value(24)
        return

    def _mode3(self):
        self.show_message('_mode3 is active')
        num_tracks = 4
        num_scenes = 2
        self._session = SessionComponent(num_tracks, num_scenes)
        track_offset = self.current_track_offset
        scene_offset = self.current_scene_offset
        self._session.set_offsets(track_offset, scene_offset)
        self._session._reassign_scenes()
        self.set_highlighting_session_component(self._session)
        session_buttons = [25,
                           26,
                           27,
                           28,
                           29,
                           30,
                           31,
                           32]
        session_channels = [0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0]
        session_types = [MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE]
        session_is_momentary = [1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1]
        self._pads = [ButtonElement(session_is_momentary[index], session_types[index], session_channels[index],
                                    session_buttons[index]) for index in range(num_tracks * num_scenes)]
        self._grid = ButtonMatrixElement(
            rows=[self._pads[index * num_tracks:index * num_tracks + num_tracks] for index in range(num_scenes)])
        self._session.set_clip_launch_buttons(self._grid)
        self._session._enable_skinning()
        self._session.set_stop_clip_triggered_value(3)
        self._session.set_stop_clip_value(8)
        for scene_index in range(num_scenes):
            scene = self._session.scene(scene_index)
            for track_index in range(num_tracks):
                clip_slot = scene.clip_slot(track_index)
                clip_slot.set_triggered_to_play_value(2)
                clip_slot.set_triggered_to_record_value(1)
                clip_slot.set_record_button_value(1)
                clip_slot.set_stopped_value(9)
                clip_slot.set_started_value(2)

        self.session_down = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 37)
        self.session_down.set_on_off_values(21, 20)
        self._session.set_scene_bank_down_button(self.session_down)
        self.session_down.add_value_listener(self._reload_active_devices, identify_sender=False)
        self.session_left = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 34)
        self.session_left.set_on_off_values(21, 20)
        self._session.set_track_bank_left_button(self.session_left)
        self.session_left.add_value_listener(self._reload_active_devices, identify_sender=False)
        self.session_right = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 36)
        self.session_right.set_on_off_values(21, 20)
        self._session.set_track_bank_right_button(self.session_right)
        self.session_right.add_value_listener(self._reload_active_devices, identify_sender=False)
        self.session_up = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 35)
        self.session_up.set_on_off_values(21, 20)
        self._session.set_scene_bank_up_button(self.session_up)
        self.session_up.add_value_listener(self._reload_active_devices, identify_sender=False)
        self._session._link()
        self.refresh_state()
        self.mode3_4 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 41)
        self.mode3_4.add_value_listener(self._activate_mode4, identify_sender=False)
        self.mode3_4.send_value(22)
        self._mode3_devices()
        self.add_device_listeners()
        self.transport = TransportComponent()
        self.transport.name = 'Transport'
        stop_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 39)
        stop_button.set_on_off_values(21, 20)
        stop_button.name = 'stop_button'
        self.transport.set_stop_button(stop_button)
        play_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 38)
        play_button.set_on_off_values(1, 2)
        play_button.name = 'play_button'
        self.transport.set_play_button(play_button)
        overdub_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 40)
        overdub_button.set_on_off_values(21, 22)
        overdub_button.name = 'overdub_button'
        self.transport.set_overdub_button(overdub_button)
        metronome_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 33)
        metronome_button.set_on_off_values(26, 27)
        metronome_button.name = 'metronome_button'
        self.transport.set_metronome_button(metronome_button)
        tap_tempo_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 4)
        tap_tempo_button.name = 'tap_tempo_button'
        self.transport.set_tap_tempo_button(tap_tempo_button)
        loop_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 9)
        loop_button.set_on_off_values(22, 25)
        loop_button.name = 'loop_button'
        self.transport.set_loop_button(loop_button)
        if hasattr(self, 'mode2_3') and self.mode2_3 is not None:
            self.mode2_3.send_value(22)
        return

    def _remove_mode3(self):
        self._remove_mode3_devices()
        self.remove_device_listeners()
        self._session.set_clip_launch_buttons(None)
        self.set_highlighting_session_component(None)
        self.session_down.remove_value_listener(self._reload_active_devices)
        self._session.set_scene_bank_down_button(None)
        self.session_left.remove_value_listener(self._reload_active_devices)
        self._session.set_track_bank_left_button(None)
        self.session_right.remove_value_listener(self._reload_active_devices)
        self._session.set_track_bank_right_button(None)
        self.session_up.remove_value_listener(self._reload_active_devices)
        self._session.set_scene_bank_up_button(None)
        self.current_track_offset = self._session._track_offset
        self.current_scene_offset = self._session._scene_offset
        self._session._unlink()
        self._session = None
        self.mode3_4.send_value(0)
        self.mode3_4.remove_value_listener(self._activate_mode4)
        self.mode3_4 = None
        self.transport.set_stop_button(None)
        self.transport.set_play_button(None)
        self.transport.set_overdub_button(None)
        self.transport.set_metronome_button(None)
        self.transport.set_tap_tempo_button(None)
        self.transport.set_loop_button(None)
        self.transport = None
        if hasattr(self, 'mode2_3') and self.mode2_3 is not None:
            self.mode2_3.send_value(21)
        return

    def _mode4(self):
        self.show_message('_mode4 is active')
        num_tracks = 4
        num_scenes = 2
        self._session = SessionComponent(num_tracks, num_scenes)
        track_offset = self.current_track_offset
        scene_offset = self.current_scene_offset
        self._session.set_offsets(track_offset, scene_offset)
        self._session._reassign_scenes()
        self.set_highlighting_session_component(self._session)
        session_buttons = [25,
                           26,
                           27,
                           28,
                           29,
                           30,
                           31,
                           32]
        session_channels = [0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0]
        session_types = [MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE,
                         MIDI_NOTE_TYPE]
        session_is_momentary = [1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1,
                                1]
        self._pads = [ButtonElement(session_is_momentary[index], session_types[index], session_channels[index],
                                    session_buttons[index]) for index in range(num_tracks * num_scenes)]
        self._grid = ButtonMatrixElement(
            rows=[self._pads[index * num_tracks:index * num_tracks + num_tracks] for index in range(num_scenes)])
        self._session.set_clip_launch_buttons(self._grid)
        self._session._enable_skinning()
        self._session.set_stop_clip_triggered_value(3)
        self._session.set_stop_clip_value(8)
        for scene_index in range(num_scenes):
            scene = self._session.scene(scene_index)
            for track_index in range(num_tracks):
                clip_slot = scene.clip_slot(track_index)
                clip_slot.set_triggered_to_play_value(2)
                clip_slot.set_triggered_to_record_value(1)
                clip_slot.set_record_button_value(1)
                clip_slot.set_stopped_value(9)
                clip_slot.set_started_value(2)

        self._session._link()
        self.refresh_state()
        self.mode4_1 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 41)
        self.mode4_1.add_value_listener(self._activate_mode1, identify_sender=False)
        self.mode4_1.send_value(24)
        self._mode4_devices()
        self.add_device_listeners()
        self.nextdevice_4 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 36)
        self.nextdevice_4.add_value_listener(self._next_device_value, identify_sender=False)
        self.prevdevice_4 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 34)
        self.prevdevice_4.add_value_listener(self._prev_device_value, identify_sender=False)
        self.transport = TransportComponent()
        self.transport.name = 'Transport'
        stop_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 39)
        stop_button.set_on_off_values(21, 20)
        stop_button.name = 'stop_button'
        self.transport.set_stop_button(stop_button)
        play_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 38)
        play_button.set_on_off_values(1, 2)
        play_button.name = 'play_button'
        self.transport.set_play_button(play_button)
        overdub_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 40)
        overdub_button.set_on_off_values(21, 22)
        overdub_button.name = 'overdub_button'
        self.transport.set_overdub_button(overdub_button)
        tap_tempo_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 4)
        tap_tempo_button.name = 'tap_tempo_button'
        self.transport.set_tap_tempo_button(tap_tempo_button)
        loop_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0, 9)
        loop_button.set_on_off_values(22, 25)
        loop_button.name = 'loop_button'
        self.transport.set_loop_button(loop_button)
        if hasattr(self, 'mode3_4') and self.mode3_4 is not None:
            self.mode3_4.send_value(23)
        return

    def _remove_mode4(self):
        self._remove_mode4_devices()
        self.remove_device_listeners()
        self._session.set_clip_launch_buttons(None)
        self.set_highlighting_session_component(None)
        self.current_track_offset = self._session._track_offset
        self.current_scene_offset = self._session._scene_offset
        self._session._unlink()
        self._session = None
        self.mode4_1.send_value(0)
        self.mode4_1.remove_value_listener(self._activate_mode1)
        self.mode4_1 = None
        self.nextdevice_4.remove_value_listener(self._next_device_value)
        self.nextdevice_4 = None
        self.prevdevice_4.remove_value_listener(self._prev_device_value)
        self.prevdevice_4 = None
        self.transport.set_stop_button(None)
        self.transport.set_play_button(None)
        self.transport.set_overdub_button(None)
        self.transport.set_tap_tempo_button(None)
        self.transport.set_loop_button(None)
        self.transport = None
        if hasattr(self, 'mode3_4') and self.mode3_4 is not None:
            self.mode3_4.send_value(22)
        return

    def _mode3_devices(self):
        if len(self.mixer.selected_strip()._track.devices) > 0:
            self.device_tracktype_selected__chain_number_selected = DeviceComponent()
            device_controls = (EncoderElement(MIDI_CC_TYPE, 0, 56, _map_modes.absolute),
                               EncoderElement(MIDI_CC_TYPE, 0, 57, _map_modes.absolute),
                               EncoderElement(MIDI_CC_TYPE, 0, 58, _map_modes.absolute),
                               EncoderElement(MIDI_CC_TYPE, 0, 59, _map_modes.absolute),
                               EncoderElement(MIDI_CC_TYPE, 0, 60, _map_modes.absolute),
                               EncoderElement(MIDI_CC_TYPE, 0, 61, _map_modes.absolute),
                               EncoderElement(MIDI_CC_TYPE, 0, 62, _map_modes.absolute),
                               EncoderElement(MIDI_CC_TYPE, 0, 63, _map_modes.absolute))
            self.device_tracktype_selected__chain_number_selected.set_parameter_controls(tuple(device_controls))
            self.set_device_component(self.device_tracktype_selected__chain_number_selected)

    def _remove_mode3_devices(self):
        if hasattr(self, 'device_tracktype_selected__chain_number_selected'):
            device_controls = (None, None, None, None, None, None, None, None)
            self.device_tracktype_selected__chain_number_selected.set_parameter_controls(tuple(device_controls))
            self.set_device_component(self.device_tracktype_selected__chain_number_selected)
        return None

    def _mode4_devices(self):
        if len(self.mixer.selected_strip()._track.devices) > 0:
            self.device_tracktype_selected__chain_number_selected = DeviceComponent()
            device_controls = (EncoderElement(MIDI_CC_TYPE, 0, 56, _map_modes.absolute),
                               EncoderElement(MIDI_CC_TYPE, 0, 57, _map_modes.absolute),
                               EncoderElement(MIDI_CC_TYPE, 0, 58, _map_modes.absolute),
                               EncoderElement(MIDI_CC_TYPE, 0, 59, _map_modes.absolute),
                               EncoderElement(MIDI_CC_TYPE, 0, 60, _map_modes.absolute),
                               EncoderElement(MIDI_CC_TYPE, 0, 61, _map_modes.absolute),
                               EncoderElement(MIDI_CC_TYPE, 0, 62, _map_modes.absolute),
                               EncoderElement(MIDI_CC_TYPE, 0, 63, _map_modes.absolute))
            self.device_tracktype_selected__chain_number_selected.set_parameter_controls(tuple(device_controls))
            self.set_device_component(self.device_tracktype_selected__chain_number_selected)
            device_tracktype_selected__chain_number_selected_on_off_button = ConfigurableButtonElement(1,
                                                                                                       MIDI_NOTE_TYPE,
                                                                                                       0, 33)
            self.device_tracktype_selected__chain_number_selected.set_on_off_button(
                device_tracktype_selected__chain_number_selected_on_off_button)
            device_tracktype_selected__chain_number_selected_bank_down = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0,
                                                                                                   37)
            device_tracktype_selected__chain_number_selected_bank_down.set_on_off_values(53, 52)
            device_tracktype_selected__chain_number_selected_bank_up = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, 0,
                                                                                                 35)
            device_tracktype_selected__chain_number_selected_bank_up.set_on_off_values(55, 56)
            self.device_tracktype_selected__chain_number_selected.set_bank_nav_buttons(
                device_tracktype_selected__chain_number_selected_bank_up,
                device_tracktype_selected__chain_number_selected_bank_down)

    def _remove_mode4_devices(self):
        if hasattr(self, 'device_tracktype_selected__chain_number_selected'):
            device_controls = (None, None, None, None, None, None, None, None)
            self.device_tracktype_selected__chain_number_selected.set_parameter_controls(tuple(device_controls))
            device_tracktype_selected__chain_number_selected_on_off_button = None
            self.device_tracktype_selected__chain_number_selected.set_on_off_button(
                device_tracktype_selected__chain_number_selected_on_off_button)
            device_tracktype_selected__chain_number_selected_bank_down = None
            device_tracktype_selected__chain_number_selected_bank_up = None
            self.device_tracktype_selected__chain_number_selected.set_bank_nav_buttons(
                device_tracktype_selected__chain_number_selected_bank_up,
                device_tracktype_selected__chain_number_selected_bank_down)
            self.set_device_component(self.device_tracktype_selected__chain_number_selected)
        return

    def _mode0(self):
        self.show_message('_mode0 is active')
        self.mixer.set_crossfader_control(EncoderElement(MIDI_CC_TYPE, 0, 75, _map_modes.absolute))
        self.mixer.set_prehear_volume_control(EncoderElement(MIDI_CC_TYPE, 0, 53, _map_modes.absolute))
        self.mixer.master_strip().set_volume_control(EncoderElement(MIDI_CC_TYPE, 0, 47, _map_modes.absolute))

    def _remove_mode0(self):
        self.mixer.set_crossfader_control(None)
        self.mixer.set_prehear_volume_control(None)
        self.mixer.master_strip().set_volume_control(None)
        return

    def tempo_control_updown_mode1(self, value):
        global direction_tempo_control_updown_mode1
        global lv_tempo_control_updown_mode1
        if value == lv_tempo_control_updown_mode1 and lv_tempo_control_updown_mode1 != 0:
            if direction_tempo_control_updown_mode1 == 'up':
                self._tempo_control_up_value_mode1(1)
            elif direction_tempo_control_updown_mode1 == 'down':
                self._tempo_control_down_value_mode1(1)
            else:
                self._tempo_control_down_value_mode1(1)
        elif value > lv_tempo_control_updown_mode1 and lv_tempo_control_updown_mode1 != 0:
            self._tempo_control_up_value_mode1(1)
            direction_tempo_control_updown_mode1 = 'up'
        elif value < lv_tempo_control_updown_mode1 and lv_tempo_control_updown_mode1 != 0:
            self._tempo_control_down_value_mode1(1)
            direction_tempo_control_updown_mode1 = 'down'
        lv_tempo_control_updown_mode1 = value

    def _tempo_control_up_value_mode1(self, value):
        if value:
            if self.song().tempo < 220:
                self.song().tempo = self.song().tempo + 1

    def _tempo_control_down_value_mode1(self, value):
        if value:
            if self.song().tempo > 20:
                self.song().tempo = self.song().tempo - 1

    def update_all_ab_select_LEDs(self, value):
        offset = 0
        if hasattr(self, '_session'):
            offset = self._session._track_offset
        if active_mode == '_mode2':
            track_num = offset + 0
            state = self.song().tracks[track_num].mixer_device.crossfade_assign
            if state == 0:
                self.a_b_assign_specific_0.set_on_off_values(23, 24)
            elif state == 1:
                self.a_b_assign_specific_0.set_on_off_values(23, 24)
            elif state == 2:
                self.a_b_assign_specific_0.set_on_off_values(21, 24)
        if active_mode == '_mode2':
            track_num = offset + 1
            state = self.song().tracks[track_num].mixer_device.crossfade_assign
            if state == 0:
                self.a_b_assign_specific_1.set_on_off_values(23, 24)
            elif state == 1:
                self.a_b_assign_specific_1.set_on_off_values(23, 24)
            elif state == 2:
                self.a_b_assign_specific_1.set_on_off_values(21, 24)
        if active_mode == '_mode2':
            track_num = offset + 2
            state = self.song().tracks[track_num].mixer_device.crossfade_assign
            if state == 0:
                self.a_b_assign_specific_2.set_on_off_values(23, 24)
            elif state == 1:
                self.a_b_assign_specific_2.set_on_off_values(23, 24)
            elif state == 2:
                self.a_b_assign_specific_2.set_on_off_values(21, 24)
        if active_mode == '_mode2':
            track_num = offset + 3
            state = self.song().tracks[track_num].mixer_device.crossfade_assign
            if state == 0:
                self.a_b_assign_specific_3.set_on_off_values(23, 24)
            elif state == 1:
                self.a_b_assign_specific_3.set_on_off_values(23, 24)
            elif state == 2:
                self.a_b_assign_specific_3.set_on_off_values(21, 24)

    def tempo_fine_control_updown_mode2(self, value):
        global direction_tempo_fine_control_updown_mode2
        global lv_tempo_fine_control_updown_mode2
        if value == lv_tempo_fine_control_updown_mode2 and lv_tempo_fine_control_updown_mode2 != 0:
            if direction_tempo_fine_control_updown_mode2 == 'up':
                self._tempo_fine_control_up_value_mode2(1)
            elif direction_tempo_fine_control_updown_mode2 == 'down':
                self._tempo_fine_control_down_value_mode2(1)
            else:
                self._tempo_fine_control_down_value_mode2(1)
        elif value > lv_tempo_fine_control_updown_mode2 and lv_tempo_fine_control_updown_mode2 != 0:
            self._tempo_fine_control_up_value_mode2(1)
            direction_tempo_fine_control_updown_mode2 = 'up'
        elif value < lv_tempo_fine_control_updown_mode2 and lv_tempo_fine_control_updown_mode2 != 0:
            self._tempo_fine_control_down_value_mode2(1)
            direction_tempo_fine_control_updown_mode2 = 'down'
        lv_tempo_fine_control_updown_mode2 = value

    def _tempo_fine_control_up_value_mode2(self, value):
        if value:
            if self.song().tempo < 270:
                self.song().tempo = self.song().tempo + 0.1

    def _tempo_fine_control_down_value_mode2(self, value):
        if value:
            if self.song().tempo > 15:
                self.song().tempo = self.song().tempo - 0.1

    def add_device_listeners(self):
        num_of_tracks = len(self.song().tracks)
        value = 'add device listener'
        for index in range(num_of_tracks):
            self.song().tracks[index].view.add_selected_device_listener(self._reload_active_devices)

    def remove_device_listeners(self):
        num_of_tracks = len(self.song().tracks)
        value = 'remove device listener'
        for index in range(num_of_tracks):
            if hasattr(self.song().tracks[index].view, 'remove_selected_device_listener'):
                self.song().tracks[index].view.remove_selected_device_listener(self._reload_active_devices)

    def _reload_active_devices(self, value=None):
        self._remove_active_devices()
        self._set_active_devices()
        if hasattr(self, '_turn_on_device_select_leds'):
            self._turn_off_device_select_leds()
            self._turn_on_device_select_leds()
        if hasattr(self, '_all_prev_device_leds'):
            self._all_prev_device_leds()
        if hasattr(self, '_all_nxt_device_leds'):
            self._all_nxt_device_leds()

    def _set_active_devices(self):
        if active_mode == '_mode1' and hasattr(self, '_mode1_devices'):
            self._mode1_devices()
        elif active_mode == '_mode2' and hasattr(self, '_mode2_devices'):
            self._mode2_devices()
        elif active_mode == '_mode3' and hasattr(self, '_mode3_devices'):
            self._mode3_devices()
        elif active_mode == '_mode4' and hasattr(self, '_mode4_devices'):
            self._mode4_devices()
        elif active_mode == '_mode0' and hasattr(self, '_mode0_devices'):
            self._mode0_devices()

    def _remove_active_devices(self):
        if active_mode == '_mode1' and hasattr(self, '_mode1_devices'):
            self._remove_mode1_devices()
        elif active_mode == '_mode2' and hasattr(self, '_mode2_devices'):
            self._remove_mode2_devices()
        elif active_mode == '_mode3' and hasattr(self, '_mode3_devices'):
            self._remove_mode3_devices()
        elif active_mode == '_mode4' and hasattr(self, '_mode4_devices'):
            self._remove_mode4_devices()
        elif active_mode == '_mode0' and hasattr(self, '_mode0_devices'):
            self._remove_mode0_devices()

    def _next_device_value(self, value):
        if value > 0:
            self._selected_device = self.selected_device_idx() + 1
            if self._selected_device < len(self.song().view.selected_track.devices):
                self.song().view.select_device(self.song().view.selected_track.devices[self.selected_device_idx() + 1])

    def _all_nxt_device_leds(self):
        next_on_off = self._is_nxt_device_on_or_off()
        if hasattr(self, 'nextdevice_4'):
            if next_on_off == 'off':
                self.nextdevice_4.send_value(38)
            elif next_on_off == 'on':
                self.nextdevice_4.send_value(39)

    def _prev_device_value(self, value):
        if value > 0:
            self._device = self.song().view.selected_track.view.selected_device
            self._device_position = self.selected_device_idx()
            if self._device is not None and self._device_position > 0:
                self.song().view.select_device(self.song().view.selected_track.devices[self.selected_device_idx() - 1])
        return

    def _all_prev_device_leds(self):
        prev_on_off = self._is_prev_device_on_or_off()
        if hasattr(self, 'prevdevice_4'):
            if prev_on_off == 'off':
                self.prevdevice_4.send_value(42)
            elif prev_on_off == 'on':
                self.prevdevice_4.send_value(43)

    def _on_selected_track_changed(self):
        ControlSurface._on_selected_track_changed(self)
        self._display_reset_delay = 0
        value = 'selected track changed'
        if hasattr(self, '_set_track_select_led'):
            self._set_track_select_led()
        if hasattr(self, '_reload_active_devices'):
            self._reload_active_devices(value)
        if hasattr(self, 'update_all_ab_select_LEDs'):
            self.update_all_ab_select_LEDs(1)

    def _is_prev_device_on_or_off(self):
        self._device = self.song().view.selected_track.view.selected_device
        self._device_position = self.selected_device_idx()
        if self._device is None or self._device_position == 0:
            on_off = 'off'
        else:
            on_off = 'on'
        return on_off

    def _is_nxt_device_on_or_off(self):
        self._selected_device = self.selected_device_idx() + 1
        if self._device is None or self._selected_device == len(self.song().view.selected_track.devices):
            on_off = 'off'
        else:
            on_off = 'on'
        return on_off

    def _set_active_mode(self):
        if active_mode == '_mode1':
            self._mode1()
        elif active_mode == '_mode2':
            self._mode2()
        elif active_mode == '_mode3':
            self._mode3()
        elif active_mode == '_mode4':
            self._mode4()
        elif active_mode == '_mode0':
            self._mode0()
        if hasattr(self, '_set_track_select_led'):
            self._set_track_select_led()
        if hasattr(self, '_turn_on_device_select_leds'):
            self._turn_off_device_select_leds()
            self._turn_on_device_select_leds()
        if hasattr(self, '_all_prev_device_leds'):
            self._all_prev_device_leds()
        if hasattr(self, '_all_nxt_device_leds'):
            self._all_nxt_device_leds()
        if hasattr(self, 'update_all_ab_select_LEDs'):
            self.update_all_ab_select_LEDs(1)

    def _remove_active_mode(self):
        if active_mode == '_mode1':
            self._remove_mode1()
        elif active_mode == '_mode2':
            self._remove_mode2()
        elif active_mode == '_mode3':
            self._remove_mode3()
        elif active_mode == '_mode4':
            self._remove_mode4()
        elif active_mode == '_mode0':
            self._remove_mode0()

    def _activate_mode1(self, value):
        global active_mode
        global shift_previous_is_active
        if value > 0:
            shift_previous_is_active = 'off'
            self._remove_active_mode()
            active_mode = '_mode1'
            self._set_active_mode()

    def _activate_mode2(self, value):
        global active_mode
        global shift_previous_is_active
        if value > 0:
            shift_previous_is_active = 'off'
            self._remove_active_mode()
            active_mode = '_mode2'
            self._set_active_mode()

    def _activate_mode3(self, value):
        global active_mode
        global shift_previous_is_active
        if value > 0:
            shift_previous_is_active = 'off'
            self._remove_active_mode()
            active_mode = '_mode3'
            self._set_active_mode()

    def _activate_mode4(self, value):
        global active_mode
        global shift_previous_is_active
        if value > 0:
            shift_previous_is_active = 'off'
            self._remove_active_mode()
            active_mode = '_mode4'
            self._set_active_mode()

    def _activate_mode0(self, value):
        global active_mode
        global shift_previous_is_active
        if value > 0:
            shift_previous_is_active = 'off'
            self._remove_active_mode()
            active_mode = '_mode0'
            self._set_active_mode()

    def _activate_shift_mode1(self, value):
        global previous_shift_mode1
        global active_mode
        global shift_previous_is_active
        if value > 0:
            shift_previous_is_active = 'on'
            previous_shift_mode1 = active_mode
            self._remove_active_mode()
            active_mode = '_mode1'
            self._set_active_mode()
        elif shift_previous_is_active == 'on':
            try:
                previous_shift_mode1
            except NameError:
                self.log_message('previous shift mode not defined yet')
            else:
                self._remove_active_mode()
                active_mode = previous_shift_mode1
                self._set_active_mode()

    def _activate_shift_mode2(self, value):
        global previous_shift_mode2
        global active_mode
        global shift_previous_is_active
        if value > 0:
            shift_previous_is_active = 'on'
            previous_shift_mode2 = active_mode
            self._remove_active_mode()
            active_mode = '_mode2'
            self._set_active_mode()
        elif shift_previous_is_active == 'on':
            try:
                previous_shift_mode2
            except NameError:
                self.log_message('previous shift mode not defined yet')
            else:
                self._remove_active_mode()
                active_mode = previous_shift_mode2
                self._set_active_mode()

    def _activate_shift_mode3(self, value):
        global previous_shift_mode3
        global shift_previous_is_active
        global active_mode
        if value > 0:
            shift_previous_is_active = 'on'
            previous_shift_mode3 = active_mode
            self._remove_active_mode()
            active_mode = '_mode3'
            self._set_active_mode()
        elif shift_previous_is_active == 'on':
            try:
                previous_shift_mode3
            except NameError:
                self.log_message('previous shift mode not defined yet')
            else:
                self._remove_active_mode()
                active_mode = previous_shift_mode3
                self._set_active_mode()

    def _activate_shift_mode4(self, value):
        global shift_previous_is_active
        global active_mode
        global previous_shift_mode4
        if value > 0:
            shift_previous_is_active = 'on'
            previous_shift_mode4 = active_mode
            self._remove_active_mode()
            active_mode = '_mode4'
            self._set_active_mode()
        elif shift_previous_is_active == 'on':
            try:
                previous_shift_mode4
            except NameError:
                self.log_message('previous shift mode not defined yet')
            else:
                self._remove_active_mode()
                active_mode = previous_shift_mode4
                self._set_active_mode()

    def _activate_shift_mode0(self, value):
        global previous_shift_mode0
        global active_mode
        global shift_previous_is_active
        if value > 0:
            shift_previous_is_active = 'on'
            previous_shift_mode0 = active_mode
            self._remove_active_mode()
            active_mode = '_mode0'
            self._set_active_mode()
        elif shift_previous_is_active == 'on':
            try:
                previous_shift_mode0
            except NameError:
                self.log_message('previous shift mode not defined yet')
            else:
                self._remove_active_mode()
                active_mode = previous_shift_mode0
                self._set_active_mode()

    def _arm_follow_track_selection(self):
        for track in self.song().tracks:
            if track.can_be_armed:
                track.arm = False

        if self.song().view.selected_track.can_be_armed:
            self.song().view.selected_track.arm = True

    def selected_device_idx(self):
        self._device = self.song().view.selected_track.view.selected_device
        return self.tuple_index(self.song().view.selected_track.devices, self._device)

    def selected_track_idx(self):
        self._track = self.song().view.selected_track
        self._track_num = self.tuple_index(self.song().tracks, self._track)
        self._track_num = self._track_num + 1
        return self._track_num

    def tuple_index(self, tuple, obj):
        for i in xrange(0, len(tuple)):
            if tuple[i] == obj:
                return i

        return False

    def disconnect(self):
        super(conspiracy, self).disconnect()
