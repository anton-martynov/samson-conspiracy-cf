from .colors import PadColors, FButtonColors


class LaunchScenePadSkin:
    class Session:
        ClipStopped = PadColors.OFF
        ClipStarted = PadColors.GREEN
        ClipRecording = PadColors.RED
        ClipTriggeredPlay = PadColors.YELLOW
        ClipTriggeredRecord = PadColors.LIGHTBLUE
        ClipEmpty = PadColors.OFF
        Scene = PadColors.GREEN
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
        ClipStopped = PadColors.LIGHTBLUE
        ClipStarted = PadColors.GREEN
        ClipRecording = PadColors.RED
        ClipTriggeredPlay = PadColors.YELLOW
        ClipTriggeredRecord = PadColors.LIGHTBLUE
        ClipEmpty = PadColors.OFF
        Scene = PadColors.GREEN
        SceneTriggered = PadColors.YELLOW
        NoScene = PadColors.OFF
        StopClip = PadColors.OFF
        StopClipTriggered = PadColors.RED
        RecordButton = PadColors.OFF

    class Zooming:
        Selected = PadColors.PURPLE
        Stopped = PadColors.RED
        Playing = PadColors.GREEN
        Empty = PadColors.OFF


class FButtonSkin:
    class Session:
        StopClip = FButtonColors.OFF
        StopClipTriggered = FButtonColors.YELLOW
