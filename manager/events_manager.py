from manager.state.state import State
from manager.queue.message import Message
import heg.names as heg_names
import manager.addresses as addresses
import osc.names as osc_names

EXIT = 'exit'

class EventsManager():
    def __init__(self, heg, osc_server, queue, osc_client, display_manager):
        self.heg = heg
        self.osc_server = osc_server
        self.osc_client = osc_client
        self.queue = queue
        self.display_manager = display_manager
        self.state = State()
        self.handler = {
                heg_names.PLAY_BUTTON:  (self.play_button_handler,  addresses.PLAY),
                heg_names.EXIT_BUTTON:  (self.exit_button_handler,  addresses.EXIT),
                heg_names.MAIN_KNOB:    (self.main_knob_handler,    addresses.MAIN_KNOB),
                osc_names.TIME_CODE:    (self.time_code_handler,    addresses.TIME_CODE),
                EXIT:                   (lambda x: None,            addresses.EXIT)
            }


    def handle_events(self):
        self.running = True
        while self.running:
            message = self.queue.pop_block()

            print(message.emmiter, " - Message: ", message.content)

            self.handler[message.emmiter][0](message)


    def start(self):
        self.display_manager.start()
        self.heg.start()
        self.osc_server.start()

        self.handle_events()

        self.heg.stop()
        self.osc_server.stop()
        self.display_manager.stop()


    def play_button_handler(self, message):
        self.osc_client.send_message(self.handler[message.emmiter][1], message.content)


    def exit_button_handler(self, message):
        self.running = False
        self.queue.push(Message(EXIT, None))


    def main_knob_handler(self, message):
        self.osc_client.send_message(self.handler[message.emmiter][1], message.content)


    def time_code_handler(self, message):
        print(message.content)
        self.display_manager.print_timecode(message.content)
