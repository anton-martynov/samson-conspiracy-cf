from _Framework.Capabilities import *
from .g25 import G25


def create_instance(c_instance):
    return G25(c_instance)


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(model_name='Samson Graphite 25'),
        PORTS_KEY: [
            inport(props=[NOTES_CC, REMOTE, SCRIPT]),
            outport(props=[REMOTE, SCRIPT])
        ]
    }
