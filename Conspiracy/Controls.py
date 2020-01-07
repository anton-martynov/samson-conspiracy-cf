import Live

from _Framework.ButtonElement import ButtonElement
from _Framework.EncoderElement import EncoderElement
from _Framework.InputControlElement import MIDI_NOTE_TYPE, MIDI_CC_TYPE
from .Colors import TransportButtonColors, PadColors


class TransportButton(ButtonElement):
    """ Three transport buttons: play, stop, record. Available colors: 0 - off, black; 1 - blue """

    def __init__(self, surface, identifier, refresh_after_release=True, *a, **k):
        ButtonElement.__init__(self, True, MIDI_NOTE_TYPE, 0, identifier, *a, **k)

        self._surface = surface
        self._refresh_after_release = refresh_after_release

        self._is_on = False

        if refresh_after_release:
            self.add_value_listener(self.__value_listener)

    def disconnect(self):
        if self._refresh_after_release:
            self.remove_value_listener(self.__value_listener)

        ButtonElement.disconnect(self)

    def turn_on(self):
        self._is_on = True
        self.send_value(TransportButtonColors.BLUE.midi_value)

    def turn_off(self):
        self._is_on = False
        self.send_value(TransportButtonColors.OFF.midi_value)

    def __value_listener(self, value):
        if int(value) == 0:  # note off, button released
            if self._is_on:
                self.turn_on()


class Slider(EncoderElement):
    """ Sliders S1 .. S6 """

    def __init__(self, identifier, *a, **k):
        super(Slider, self).__init__(MIDI_CC_TYPE, 0, identifier, Live.MidiMap.MapMode.absolute, *a, **k)


class XFader(Slider):
    """ Crossfader """

    def __init__(self, *a, **k):
        super(XFader, self).__init__(15, *a, **k)


class LaunchScenePad(ButtonElement):
    """ Pad to launch scene (right (5th) column of pads 05, 10, 15, 20, 25) """

    def __init__(self, identifier, *a, **k):
        ButtonElement.__init__(self, True, MIDI_NOTE_TYPE, 0, identifier, *a, **k)


class LaunchClipPad(ButtonElement):
    """ Pad to launch clip """

    def __init__(self, identifier, *a, **k):
        ButtonElement.__init__(self, True, MIDI_NOTE_TYPE, 0, identifier, *a, **k)


class LaunchScenePadSkin:
    class Session:
        ClipStopped = PadColors.OFF
        ClipStarted = PadColors.GREEN
        ClipRecording = PadColors.RED
        ClipTriggeredPlay = PadColors.YELLOW
        ClipTriggeredRecord = PadColors.LIGHTBLUE
        ClipEmpty = PadColors.OFF
        Scene = PadColors.OFF
        SceneTriggered = PadColors.YELLOW
        NoScene = PadColors.OFF
        StopClip = PadColors.OFF
        StopClipTriggered = PadColors.YELLOW
        RecordButton = PadColors.OFF

    class Zooming:
        Selected = PadColors.PURPLE
        Stopped = PadColors.RED
        Playing = PadColors.GREEN
        Empty = PadColors.OFF


class LaunchClipPadSkin:
    class Session:
        ClipStopped = PadColors.OFF
        ClipStarted = PadColors.GREEN
        ClipRecording = PadColors.RED
        ClipTriggeredPlay = PadColors.YELLOW
        ClipTriggeredRecord = PadColors.LIGHTBLUE
        ClipEmpty = PadColors.OFF
        Scene = PadColors.OFF
        SceneTriggered = PadColors.YELLOW
        NoScene = PadColors.OFF
        StopClip = PadColors.OFF
        StopClipTriggered = PadColors.YELLOW
        RecordButton = PadColors.OFF

    class Zooming:
        Selected = PadColors.PURPLE
        Stopped = PadColors.RED
        Playing = PadColors.GREEN
        Empty = PadColors.OFF
