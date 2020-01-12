import Live
import logging

from _Framework.EncoderElement import EncoderElement
from _Framework.InputControlElement import MIDI_CC_TYPE


class Slider(EncoderElement):
    """ SYSEX (127, 127, 4, 1) + value """

    def __init__(self):
        EncoderElement.__init__(self, MIDI_CC_TYPE, 0, 121, Live.MidiMap.MapMode.absolute)


class Encoder(EncoderElement):

    def __init__(self, channel, cc_identifier, name):
        EncoderElement.__init__(self, MIDI_CC_TYPE, channel, cc_identifier, Live.MidiMap.MapMode.absolute, name=name)

        self._log = logging.getLogger('Graphite25_Encoder[Ch%d, CC=%d]' % (channel, cc_identifier))

    def send_midi(self, message):
        self._log.info('AL sends midi message: %s' % message)

        EncoderElement.send_midi(self, message)
