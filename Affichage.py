import ssd1306
import time

def oledTemp(oled,temperature):
    oled.fill(0)
    oled.fill_rect(0, 0, 32, 32, 1)
    oled.fill_rect(2, 2, 28, 28, 0)
    oled.vline(9, 8, 22, 1)
    oled.vline(16, 2, 22, 1)
    oled.vline(23, 8, 22, 1)
    oled.fill_rect(26, 24, 2, 4, 1)
    oled.text('TEMPERATURE', 40, 0)
    oled.text(str(temperature), 40, 20)
    oled.pixel(91, 20,1)
    oled.pixel(90, 21,1)
    oled.pixel(90, 22,1)
    oled.pixel(91, 23,1)
    oled.pixel(92, 21,1)
    oled.pixel(92, 22,1)
    oled.text('C', 96, 20)
    oled.show()
    time.sleep(5)
    oled.fill(0)
    oled.show()
