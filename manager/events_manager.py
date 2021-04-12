from manager.state.state import State
from manager.queue.message import Message

class EventsManager():
    def __init__(self, heg, osc_server, queue, osc_client, display_manager):
        self.heg = heg
        self.osc_server = osc_server
        self.osc_client = osc_client
        self.queue = queue
        self.display_manager = display_manager
        self.state = State()

    def handle_events(self):
        running = True
        while running:
            message = self.queue.pop_block()
            print("Message: ", message.message)
            if message.message == 'exit':
                running = False

    def start(self):
        self.display_manager.init()

        self.heg.start()
        self.osc_server.start()

        self.handle_events()

        self.heg.stop()
        self.osc_server.stop()
