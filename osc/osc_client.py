from pythonosc.udp_client import SimpleUDPClient

class OSCClient():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client = SimpleUDPClient(ip, port)


    def send_message(self, address, message):
        self.client.send_message(address, message)
