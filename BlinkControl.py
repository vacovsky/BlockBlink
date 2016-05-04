from RPi import GPIO
import time


class BlinkControl:

    def __init__(self):
        GPIO.cleanup()
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)

    def blink(self, base_color="green", flash_color="red", count=1, interval=0.05):
        blinked = 0
        while blinked <= count:
            time.sleep(interval)
            if base_color == "green":
                self.blink_green()
            elif base_color == "red":
                self.blink_red()
            elif base_color == "purple":
                self.blink_purple()
            elif base_color == "teal":
                self.blink_teal()
            elif base_color == "green":
                self.blink_green()
            elif base_color == "blue":
                self.blink_blue()
            elif base_color == "white":
                self.blink_white()
            elif base_color == "yellow":
                self.blink_yellow()
            elif base_color == "off":
                self.blink_off()

            time.sleep(interval)
            if base_color == "green":
                self.blink_green()
            elif base_color == "red":
                self.blink_red()
            elif base_color == "purple":
                self.blink_purple()
            elif base_color == "teal":
                self.blink_teal()
            elif base_color == "green":
                self.blink_green()
            elif base_color == "blue":
                self.blink_blue()
            elif base_color == "white":
                self.blink_white()
            elif base_color == "yellow":
                self.blink_yellow()
            elif base_color == "off":
                self.blink_off()

            blinked += 1
            print(blinked)
            #GPIO.cleanup()

    """
    17 = green, 22 = blue, 27 = red
    """

    def blink_blue(self):
        GPIO.output(17, 0)
        GPIO.output(27, 0)
        GPIO.output(22, 1)

    def blink_red(self):
        GPIO.output(17, 0)
        GPIO.output(27, 1)
        GPIO.output(22, 0)

    def blink_yellow(self):
        GPIO.output(17, 1)
        GPIO.output(27, 1)
        GPIO.output(22, 0)

    def blink_green(self):
        GPIO.output(17, 1)
        GPIO.output(27, 0)
        GPIO.output(22, 0)

    def blink_white(self):
        GPIO.output(17, 1)
        GPIO.output(27, 1)
        GPIO.output(22, 1)

    def blink_purple(self):
        GPIO.output(17, 0)
        GPIO.output(27, 1)
        GPIO.output(22, 1)

    def blink_teal(self):
        GPIO.output(17, 1)
        GPIO.output(27, 0)
        GPIO.output(22, 1)

    def blink_off(self):
        GPIO.output(17, 0)
        GPIO.output(27, 0)
        GPIO.output(22, 0)


if __name__ == '__main__':
    BlinkControl().blink(base_color="off", flash_color="yellow", count=100, interval=0.05)
