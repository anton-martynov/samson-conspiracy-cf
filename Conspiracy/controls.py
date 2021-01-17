import logging

import Live
from _Framework.ButtonElement import ButtonElement, Skin
from _Framework.EncoderElement import EncoderElement
from _Framework.InputControlElement import MIDI_NOTE_TYPE, MIDI_CC_TYPE

from .colors import TransportButtonColors, FButtonColors
from .skins import LaunchClipPadSkin, LaunchScenePadSkin, SelectModeButtonSkin, DeviceFButtonSkin


class ControlWithRefreshLightAfterNoteOff(ButtonElement):
    def __init__(self, identifier, skin, refresh_after_release=True, *a, **k):
        ButtonElement.__init__(self, True, MIDI_NOTE_TYPE, 0, identifier, skin, *a, **k)
        self._refresh_after_release = refresh_after_release

        if self._refresh_after_release:
            self.add_value_listener(self.__value_listener)

        self.set_report_values(False, False)

    def disconnect(self):
        if self._refresh_after_release:
            self.remove_value_listener(self.__value_listener)

        ButtonElement.disconnect(self)

    def __value_listener(self, value):
        if int(value) == 0:  # note off, button released
            self.refresh_after_release()

    def refresh_after_release(self):
        pass

    def _report_value(self, value, is_input):
        self._verify_value(value)
        message = str(self.__class__.__name__) + u' ('
        if self._msg_type == MIDI_NOTE_TYPE:
            message += u'Note ' + str(self._msg_identifier) + u', '
        elif self._msg_type == MIDI_CC_TYPE:
            message += u'CC ' + str(self._msg_identifier) + u', '
        else:
            message += u'PB '
        message += u'Chan. ' + str(self._msg_channel)
        message += u') '
        message += u'received value ' if is_input else u'sent value '
        message += str(value)
        logging.getLogger(str(self.__class__.__name__)).info(message)


class ButtonWithRefreshLightAfterNoteOff(ControlWithRefreshLightAfterNoteOff):
    def __init__(self, identifier, skin, refresh_after_release=True, *a, **k):
        ControlWithRefreshLightAfterNoteOff.__init__(self, identifier, skin, refresh_after_release, *a, **k)

        self._last_on = False
        self._color_on = None
        self._color_off = None

    def turn_on(self):
        self._last_on = True
        self.send_value(self._color_on)

    def turn_off(self):
        self._last_on = False
        self.send_value(self._color_off)

    def refresh_after_release(self):
        self.turn_on()


class TransportButton(ButtonWithRefreshLightAfterNoteOff):
    """ Three transport buttons: play, stop, record. Available colors: 0 - off, black; 1 - blue """

    def __init__(self, identifier, refresh_after_release=True, *a, **k):
        ButtonWithRefreshLightAfterNoteOff.__init__(self, identifier, Skin(), refresh_after_release, *a, **k)

        self._color_on = TransportButtonColors.BLUE
        self._color_off = TransportButtonColors.OFF


class FButton(ButtonWithRefreshLightAfterNoteOff):
    """ F-buttons """

    def __init__(self, identifier, refresh_after_release=True, *a, **k):
        ButtonWithRefreshLightAfterNoteOff.__init__(self, identifier, refresh_after_release, *a, **k)

        self._color_on = FButtonColors.YELLOW
        self._color_off = FButtonColors.OFF


class DeviceFButton(ControlWithRefreshLightAfterNoteOff):
    """ F5, F6 - prev/next device navigation """
    def __init__(self, identifier, *a, **k):
        ControlWithRefreshLightAfterNoteOff.__init__(self, identifier, Skin(DeviceFButtonSkin), True, *a, **k)

    def set_light(self, value):
        logging.getLogger(str(self.__class__.__name__)).info("set_light:" + str(value))
        ControlWithRefreshLightAfterNoteOff.set_light(self, value)

    def turn_off(self):
        logging.getLogger(str(self.__class__.__name__)).info("turn_off")
        ControlWithRefreshLightAfterNoteOff.turn_off(self)

    def turn_on(self):
        logging.getLogger(str(self.__class__.__name__)).info("turn_on")
        ControlWithRefreshLightAfterNoteOff.turn_on(self)


class TrackNavigationFButton(FButton):
    """ F-buttons """

    def __init__(self, identifier, *a, **k):
        FButton.__init__(self, identifier, False, *a, **k)

        self._color_on = FButtonColors.OFF
        self._color_off = FButtonColors.OFF


class NavButton(ButtonElement):
    """ Four navigation buttons: left, right, up, down Available colors: 0 - off, black; 1 - blue """

    def __init__(self, identifier, *a, **k):
        ButtonElement.__init__(self, True, MIDI_NOTE_TYPE, 0, identifier, *a, **k)

    def turn_on(self):
        self.send_value(TransportButtonColors.BLUE.midi_value)

    def turn_off(self):
        self.send_value(TransportButtonColors.OFF.midi_value)


class Slider(EncoderElement):
    """ Sliders S1 .. S6 """

    def __init__(self, identifier, *a, **k):
        super(Slider, self).__init__(MIDI_CC_TYPE, 0, identifier, Live.MidiMap.MapMode.absolute, *a, **k)


class Encoder(EncoderElement):
    """ Encoders/knobs E1-E8 """

    def __init__(self, identifier, *a, **k):
        super(Encoder, self).__init__(MIDI_CC_TYPE, 0, identifier, Live.MidiMap.MapMode.absolute, *a, **k)
        self.set_report_values(False, False)

    def _report_value(self, value, is_input):
        self._verify_value(value)
        message = str(self.__class__.__name__) + u' ('
        if self._msg_type == MIDI_NOTE_TYPE:
            message += u'Note ' + str(self._msg_identifier) + u', '
        elif self._msg_type == MIDI_CC_TYPE:
            message += u'CC ' + str(self._msg_identifier) + u', '
        else:
            message += u'PB '
        message += u'Chan. ' + str(self._msg_channel)
        message += u') '
        message += u'received value ' if is_input else u'sent value '
        message += str(value)
        logging.getLogger().info(message)


class XFader(Encoder):
    """ Crossfader """

    def __init__(self, *a, **k):
        super(XFader, self).__init__(15, *a, **k)


class PadWithRefreshLightAfterNoteOff(ControlWithRefreshLightAfterNoteOff):
    def __init__(self, identifier, skin, *a, **k):
        ControlWithRefreshLightAfterNoteOff.__init__(self, identifier, skin, True, *a, **k)

        self._last_light = None

    def refresh_after_release(self):
        if self._last_light:
            self.set_light(self._last_light)

    def set_light(self, value):
        ControlWithRefreshLightAfterNoteOff.set_light(self, value)
        self._last_light = value

    def turn_off(self):
        ControlWithRefreshLightAfterNoteOff.turn_off(self)
        self._last_light = None


class LaunchScenePad(PadWithRefreshLightAfterNoteOff):
    """ Pad to launch scene (right (5th) column of pads) """

    def __init__(self, identifier, *a, **k):
        PadWithRefreshLightAfterNoteOff.__init__(self, identifier, Skin(LaunchScenePadSkin), *a, **k)


class LaunchClipPad(PadWithRefreshLightAfterNoteOff):
    """ Pad to launch clip """

    def __init__(self, identifier, *a, **k):
        PadWithRefreshLightAfterNoteOff.__init__(self, identifier, Skin(LaunchClipPadSkin), *a, **k)


class SelectModeButton(PadWithRefreshLightAfterNoteOff):
    def __init__(self, identifier, *a, **k):
        PadWithRefreshLightAfterNoteOff.__init__(self, identifier, Skin(SelectModeButtonSkin), *a, **k)
