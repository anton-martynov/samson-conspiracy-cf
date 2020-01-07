from _Framework.Capabilities import *
from .Conspiracy import Conspiracy


def create_instance(c_instance):
    return Conspiracy(c_instance)


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(model_name='Samson Conspiracy'),
        PORTS_KEY: [
            inport(props=[NOTES_CC, REMOTE, SCRIPT]),
            outport(props=[NOTES_CC, REMOTE, SCRIPT])
        ]
    }
