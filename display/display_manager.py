from libs.I2C_LCD_driver import lcd

class DisplayManager():
    def __init__(self):
        self.lcd = lcd()


    def init(self):
        print("DisplayManager Initialized")
        self.lcd.lcd_clear()
        self.lcd.lcd_display_string(u"Hello world!")
