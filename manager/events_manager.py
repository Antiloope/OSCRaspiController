from manager.state.state import get_initial_state
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
        self.state = get_initial_state(self)
        self.addresses = {
                heg_names.PLAY_BUTTON:  addresses.PLAY,
                heg_names.EXIT_BUTTON:  addresses.EXIT,
                heg_names.MAIN_KNOB:    addresses.MAIN_KNOB,
                osc_names.TIME_CODE:    addresses.TIME_CODE
            }


    def handle_events(self):
        self.running = True
        while self.running:
            message = self.queue.pop_block()

            print(message.emmiter, " - Message: ", message.content)

            self.state.handle(message)


    def start(self):
        self.display_manager.start()
        self.heg.start()
        self.osc_server.start()

        self.handle_events()

        self.heg.stop()
        self.osc_server.stop()
        self.display_manager.stop()


    def play_button_handler(self, message):
        self.osc_client.send_message(self.addresses[message.emmiter], message.content)


    def exit_button_handler(self, message):
        self.running = False
        self.queue.push(Message(EXIT, None))


    def main_knob_handler(self, message):
        self.osc_client.send_message(self.addresses[message.emmiter], message.content)


    def time_code_handler(self, message):
        self.display_manager.print_timecode(message.content)
