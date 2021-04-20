import heg.definitions as hdef
import heg.names as names

class HEG():
    def __init__(self, queue):
        self.queue = queue
        self.hardware = [
                hdef.PlayButton(self.queue, names.PLAY_BUTTON_PIN),
                hdef.ExitButton(self.queue, names.EXIT_BUTTON_PIN),
                hdef.MainKnob(self.queue, names.MAIN_KNOB_PINA, names.MAIN_KNOB_PINB)
            ]


    def start(self):
        for i in self.hardware:
            i.init()

        print("HEG started")


    def stop(self):
        for i in self.hardware:
            i.disable()

        print("HEG stopped")
