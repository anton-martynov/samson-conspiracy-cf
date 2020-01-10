import logging

import Live
from _Framework.ButtonElement import ButtonElement, Skin
from _Framework.EncoderElement import EncoderElement
from _Framework.InputControlElement import MIDI_NOTE_TYPE, MIDI_CC_TYPE

from .colors import TransportButtonColors, FButtonColors
from .skins import LaunchClipPadSkin, LaunchScenePadSkin


class ButtonWithRefreshLightAfterNoteOff(ButtonElement):
    def __init__(self, identifier, refresh_after_release=True, *a, **k):
        ButtonElement.__init__(self, True, MIDI_NOTE_TYPE, 0, identifier, *a, **k)

        self._refresh_after_release = refresh_after_release
        self._last_on = False

        self._color_on = 1
        self._color_off = 0

        if self._refresh_after_release:
            self.add_value_listener(self.__value_listener)

    def disconnect(self):
        if self._refresh_after_release:
            self.remove_value_listener(self.__value_listener)

        ButtonElement.disconnect(self)

    def turn_on(self):
        self._last_on = True
        self.send_value(self._color_on)

    def turn_off(self):
        self._last_on = False
        self.send_value(self._color_off)

    def __value_listener(self, value):
        if int(value) == 0:  # note off, button released
            if self._last_on:
                self.turn_on()


class TransportButton(ButtonWithRefreshLightAfterNoteOff):
    """ Three transport buttons: play, stop, record. Available colors: 0 - off, black; 1 - blue """

    def __init__(self, identifier, refresh_after_release=True, *a, **k):
        ButtonWithRefreshLightAfterNoteOff.__init__(self, identifier, refresh_after_release, *a, **k)

        self._color_on = TransportButtonColors.BLUE
        self._color_off = TransportButtonColors.OFF


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


class XFader(Slider):
    """ Crossfader """

    def __init__(self, *a, **k):
        super(XFader, self).__init__(15, *a, **k)


class PadWithRefreshLightAfterNoteOff(ButtonElement):
    def __init__(self, identifier, skin, *a, **k):
        ButtonElement.__init__(self, True, MIDI_NOTE_TYPE, 0, identifier, skin, *a, **k)

        self._last_light = None
        self.add_value_listener(self.__value_listener)

        self._logger = logging.getLogger(self.__class__.__name__ + '-' + str(identifier))

    def disconnect(self):
        self.remove_value_listener(self.__value_listener)

        ButtonElement.disconnect(self)

    def __value_listener(self, value):
        if int(value) == 0:  # note off, button released
            self._logger.info('__value_listener.value = ' + str(value))

            if self._last_light:
                self.set_light(self._last_light)

    def set_light(self, value):
        self._logger.info('set_light.value = ' + str(value))

        ButtonElement.set_light(self, value)
        self._last_light = value

    def turn_off(self):
        self._logger.info('turn_off')

        ButtonElement.turn_off(self)
        self._last_light = None


class LaunchScenePad(PadWithRefreshLightAfterNoteOff):
    """ Pad to launch scene (right (5th) column of pads 05, 10, 15, 20, 25) """

    def __init__(self, identifier, *a, **k):
        PadWithRefreshLightAfterNoteOff.__init__(self, identifier, Skin(LaunchScenePadSkin), *a, **k)


class LaunchClipPad(PadWithRefreshLightAfterNoteOff):
    """ Pad to launch clip """

    def __init__(self, identifier, *a, **k):
        PadWithRefreshLightAfterNoteOff.__init__(self, identifier, Skin(LaunchClipPadSkin), *a, **k)


class FButton(ButtonWithRefreshLightAfterNoteOff):
    """ F-buttons """

    def __init__(self, identifier, *a, **k):
        ButtonWithRefreshLightAfterNoteOff.__init__(self, identifier, True, *a, **k)

        self._color_on = FButtonColors.YELLOW
        self._color_off = FButtonColors.OFF
