from manager.queue.message import Message
from gpiozero import Button, RotaryEncoder
import heg.names as names

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



class Rotary(HardwareDevice):
    def __init__(self, queue, pinA, pinB):
        self.pinA = pinA
        self.pinB = pinB
        self.queue = queue
        self.rotary_encoder = RotaryEncoder(self.pinA,self.pinB, max_steps=0)


    def init(self):
        pass


    def disable(self):
        self.rotary_encoder.when_rotated = None
        self.rotary_encoder.when_rotated_clockwise = None
        self.rotary_encoder.when_rotated_counter_clockwise = None



class PlayButton(Btn):
    def __init__(self, queue, pin):
        super().__init__(queue, pin)
        self.status = 0
        self.device = names.PLAY_BUTTON


    def when_pressed(self):
        if self.status is 1:
            self.status = 0
        else:
            self.status = 1
        self.queue.push(Message(self.device, self.status))


    def init(self):
        self.button.when_pressed = self.when_pressed



class ExitButton(Btn):
    def __init__(self, queue, pin):
        super().__init__(queue, pin)
        self.device = names.EXIT_BUTTON


    def when_pressed(self):
        self.queue.push(Message(self.device, None))


    def init(self):
        self.button.when_pressed = self.when_pressed



class MainKnob(Rotary):
    def __init__(self, queue, pinA, pinB):
        super().__init__(queue, pinA, pinB)
        self.device = names.MAIN_KNOB


    def when_rotated_clockwise(self):
        self.queue.push(Message(self.device,0.05))


    def when_rotated_counter_clockwise(self):
        self.queue.push(Message(self.device,-0.05))


    def init(self):
        self.rotary_encoder.when_rotated_clockwise = self.when_rotated_clockwise
        self.rotary_encoder.when_rotated_counter_clockwise = self.when_rotated_counter_clockwise
