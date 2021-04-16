import threading
from manager.queue.message import Message
from gpiozero import Button, RotaryEncoder
from signal import pause
import heg.definitions as hdef

rotor = RotaryEncoder(20,21, max_steps=0)

class HardwareDevice():
    def __init__(self):
        pass

    
    def init(self):
        pass


    def disable(self):
        pass


class Btn(HardwareDevice):
    def __init__(self, queue, pin):
        self.pin = pin
        self.queue = queue
        self.button = Button(pin)


    def init(self):
        pass


    def disable(self):
        self.button.when_pressed = None
        self.button.when_held = None
        self.button.when_released = None


class PlayButton(Btn):
    def __init__(self, queue, pin):
        super().__init__(queue, pin)
        self.status = 0
        self.device = hdef.PLAY_BUTTON 


    def when_pressed(self):
        if self.status is 1:
            self.status = 0
        else:
            self.status = 1
        self.queue.push(Message(self.device, self.status))


    def init(self):
        self.button.when_pressed = self.when_pressed


    def disable(self):
        self.button.when_pressed = None


class ExitButton(Btn):
    def __init__(self, queue, pin):
        super().__init__(queue, pin)
        self.device = hdef.EXIT_BUTTON 


    def when_pressed(self):
        self.queue.push(Message(self.device, None))


    def init(self):
        self.button.when_pressed = self.when_pressed


    def disable(self):
        self.button.when_pressed = None


class HEG():
    def __init__(self, queue):
        self.queue = queue
        self.valor = 1
        self.hardware = [
                PlayButton(self.queue, 4),
                ExitButton(self.queue, 17)
            ]


    def rotor_rotated_clockwise(self):
        self.queue.push(Message(0.05))


    def rotor_rotated_counterwise(self):
        self.queue.push(Message(-0.05))


    def start(self):
        for i in self.hardware:
            i.init()

        rotor.when_rotated_clockwise = self.rotor_rotated_clockwise
        rotor.when_rotated_counter_clockwise = self.rotor_rotated_counterwise
        print("HEG started")


    def stop(self):
        for i in self.hardware:
            i.disable()

        rotor.when_rotated_counter_clockwise = None
        rotor.when_rotated_clockwise = None
        print("HEG stopped")

