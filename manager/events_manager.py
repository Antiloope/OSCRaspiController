from manager.state.state import State

class EventsManager():
    def __init__(self, heg, osc_server, queue, osc_client, display_manager):
        self.heg = heg
        self.osc_server = osc_client
        self.osc_client = osc_client
        self.queue = queue
        self.display_manager = display_manager
        self.state = State()

    def start(self):
        pass
