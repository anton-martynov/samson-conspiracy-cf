from .colors import PadColors, FButtonColors


class LaunchScenePadSkin:
    class Session:
        ClipStopped = PadColors.YELLOW
        ClipStarted = PadColors.GREEN
        ClipRecording = PadColors.RED
        ClipTriggeredPlay = PadColors.GREEN_BLINK
        ClipTriggeredRecord = PadColors.RED_BLINK
        ClipEmpty = PadColors.OFF
        Scene = PadColors.OFF
        SceneTriggered = PadColors.GREEN_BLINK
        NoScene = PadColors.OFF
        StopClip = PadColors.OFF
        StopClipTriggered = PadColors.GREEN_BLINK
        RecordButton = PadColors.OFF

    class Zooming:
        Selected = PadColors.YELLOW
        Stopped = PadColors.RED
        Playing = PadColors.GREEN
        Empty = PadColors.OFF


class LaunchClipPadSkin:
    class Session:
        Scene = PadColors.GREEN
        SceneTriggered = PadColors.LIGHTBLUE  # PadColors.GREEN_BLINK
        NoScene = PadColors.OFF
        ClipStopped = PadColors.YELLOW
        ClipStarted = PadColors.GREEN
        ClipRecording = PadColors.RED
        ClipTriggeredPlay = PadColors.GREEN_BLINK
        ClipTriggeredRecord = PadColors.RED_BLINK
        ClipEmpty = PadColors.OFF
        RecordButton = PadColors.RED
        StopClip = PadColors.OFF
        StopClipTriggered = PadColors.RED_BLINK
        StoppedClip = PadColors.LIGHTBLUE

    class Zooming:
        Selected = PadColors.PURPLE
        Stopped = PadColors.RED
        Playing = PadColors.GREEN
        Empty = PadColors.OFF


class FButtonSkin:
    class Mixer:
        TrackSelected = FButtonColors.YELLOW
        TrackUnselected = FButtonColors.OFF

    class Session:
        TrackSelected = FButtonColors.YELLOW
        TrackUnselected = FButtonColors.OFF

    class DefaultButton:
        On = FButtonColors.YELLOW
        Off = FButtonColors.OFF
        Disabled = FButtonColors.OFF


class SelectModeButtonSkin:
    class Session:
        StopClip = FButtonColors.GREEN
        StopClipTriggered = FButtonColors.YELLOW


class DeviceFButtonSkin:
    class DefaultButton:
        On = FButtonColors.YELLOW
        Off = FButtonColors.OFF
        Disabled = FButtonColors.OFF
