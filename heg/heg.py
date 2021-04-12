import threading
from manager.queue.message import Message
from gpiozero import Button
from signal import pause

button = Button(2)

class HEG():
    def __init__(self, queue):
        self.queue = queue


    def button_message(self):
        self.queue.push(Message("Button pressed"))


    def start(self):
        button.when_pressed = self.button_message
        print("HEG started")


    def stop(self):
        button.when_pressed = None
        print("HEG stopped")
