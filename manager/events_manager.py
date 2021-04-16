from manager.state.state import State
from manager.queue.message import Message
import asyncio
import heg.definitions as hdef

class EventsManager():
    def __init__(self, heg, osc_server, queue, osc_client, display_manager):
        self.heg = heg
        self.osc_server = osc_server
        self.osc_client = osc_client
        self.queue = queue
        self.display_manager = display_manager
        self.state = State()
        self.handler = {
                hdef.PLAY_BUTTON: (self.play_button_handler, '/play'),
                hdef.EXIT_BUTTON: (self.exit_button_handler, None)
            }


    def handle_events(self):
        self.running = True
        while self.running:
            message = self.queue.pop_block()
            
            print(message.emmiter, " - Message: ", message.content)
            
            self.handler[message.emmiter][0](message)


    def start(self):
        self.display_manager.init()

        self.heg.start()
        self.osc_server.start()

        self.handle_events()

        self.heg.stop()
        self.osc_server.stop()


    def play_button_handler(self, message):
        self.osc_client.send_message(self.handler[message.emmiter][1], message.content)


    def exit_button_handler(self, message):
        self.running = False
