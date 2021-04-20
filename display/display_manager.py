from libs.I2C_LCD_driver import lcd

class DisplayManager():
    def __init__(self):
        self.lcd = lcd()


    def init(self):
        print("DisplayManager Initialized")
        self.lcd.backlight(1)
        self.lcd.lcd_clear()
        self.lcd.lcd_display_string(u"    OSCRaspi    ",1)
        self.lcd.lcd_display_string(u"     Hello!     ",2)


    def bye(self):
        self.lcd.backlight(0)
        self.lcd.lcd_clear()
        self.lcd.lcd_display_string(u"    OSCRaspi    ",1)
        self.lcd.lcd_display_string(u"      Bye!      ",2)


    def print_timecode(self, timecode):
        self.lcd.lcd_display_string(u" Timecode:      ",1)
        self.lcd.lcd_display_string(timecode, 2)
