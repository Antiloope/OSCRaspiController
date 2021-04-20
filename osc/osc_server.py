from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from multiprocessing import Process
from manager.queue.message import Message
import manager.addresses as addresses
import osc.names as names

class OSCServer():
    def time_code_handler(self, address, *args):
        current_timecode = int(args[0].replace(' ',''))
        if( abs(current_timecode - self.timecode_buffer) > 160 ):
            self.queue.push(Message(names.TIME_CODE,args[0]))
            self.timecode_buffer = current_timecode


    def __init__(self, ip, port, queue):
        self.ip = ip.strip()
        self.port = port
        self.queue = queue
        self.dispatcher = Dispatcher()
        self.dispatcher.map(addresses.TIME_CODE,self.time_code_handler)
        self.timecode_buffer = 0


    def start(self):
        self.server = BlockingOSCUDPServer((self.ip, self.port), self.dispatcher)
        self.process = Process(target=self.server.serve_forever)
        self.process.start()
        print("OSCServer started ", self.ip, self.port)


    def stop(self):
        self.process.terminate()
        print("OSCServer stopped")
