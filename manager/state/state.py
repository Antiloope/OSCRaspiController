import heg.names as heg_names
import osc.names as osc_names

EXIT = 'exit'

class State():
    def __init__(self, manager):
        self.handler = None


    def handle(self, message):
        self.handler[message.emmiter](message)



class InitialState(State):
    def __init__(self, manager):
        self.handler = {
                heg_names.PLAY_BUTTON:  manager.play_button_handler,
                heg_names.EXIT_BUTTON:  manager.exit_button_handler,
                heg_names.MAIN_KNOB:    manager.main_knob_handler,
                osc_names.TIME_CODE:    manager.time_code_handler,
                EXIT:                   lambda x: None
            }



def get_initial_state(manager):
    return InitialState(manager)
