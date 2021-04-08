import queue as q

QUEUE_CLASS_TYPE = q.Queue

'''
EventsQueue

This class encapsulates a queue to send messages between threads.
'''
class EventsQueue():
    def __init__(self):
        self.queue = QUEUE_CLASS_TYPE()

    def push(self, message):
        self.queue.put_nowait(message)

    def pop(self):
        return self.queue.get_nowait()

    def pop_block(self):
        return self.queue.get(block = True)
