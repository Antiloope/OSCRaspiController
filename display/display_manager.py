from libs.I2C_LCD_driver import lcd
from manager.queue.events_queue import EventsQueue
from multiprocessing import Process
import display.names as names
from manager.queue.message import Message

EXIT = 'exit'

class DisplayManager():
    def __init__(self):
        self.lcd = lcd()
        self.queue = EventsQueue()
        self.handler = {
                names.TIME_CODE:        self.print_timecode_handler,
                EXIT:                   lambda x: True
            }


    def display_loop(self):
        self.lcd.lcd_clear()
        self.lcd.lcd_display_string(u"    OSCRaspi    ",1)
        self.lcd.lcd_display_string(u"     Hello!     ",2)

        while True:
            message = self.queue.pop_block()

            print(message.emmiter, " - Display message: ", message.content)

            if self.handler[message.emmiter](message): break

        self.lcd.lcd_clear()
        self.lcd.lcd_display_string(u"    OSCRaspi    ",1)
        self.lcd.lcd_display_string(u"      Bye!      ",2)


    def start(self):
        print("DisplayManager Initialized")
        self.process = Process(target=self.display_loop)
        self.process.start()


    def stop(self):
        self.queue.push(Message(EXIT, None))


    def print_timecode_handler(self, message):
        self.lcd.lcd_display_string(u" Timecode:      ",1)
        self.lcd.lcd_display_string(message.content, 2)


    def print_timecode(self, timecode):
        self.queue.push(Message(names.TIME_CODE, timecode))
