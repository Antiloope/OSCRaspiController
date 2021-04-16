from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import asyncio
from multiprocessing import Process
from manager.queue.message import Message

class OSCServer():
    def handler(self, address, *args):
        self.queue.push(Message(args[0]))


    def __init__(self, ip, port, queue):
        self.ip = ip.strip()
        self.port = port
        self.queue = queue
        self.dispatcher = Dispatcher()
        self.dispatcher.map('/prueba',self.handler)


    def start(self):
        print("OSCServer started ", self.ip, self.port)
        self.server = BlockingOSCUDPServer((self.ip, self.port), self.dispatcher)
        self.thread = Process(target=self.server.serve_forever)
        self.thread.start()


    def stop(self):
        print("OSCServer stopped")
        self.thread.terminate()
