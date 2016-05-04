from RPi import GPIO
import time


class BlinkControl:

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)

    def blink(self, base_color="green", flash_color="red", count=1, interval=0.05):
        blinked = 0
        while blinked <= count:
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

            if flash_color == "green":
                self.blink_green()
            elif flash_color == "red":
                self.blink_red()
            elif flash_color == "purple":
                self.blink_purple()
            elif flash_color == "teal":
                self.blink_teal()
            elif flash_color == "green":
                self.blink_green()
            elif flash_color == "blue":
                self.blink_blue()
            elif flash_color == "white":
                self.blink_white()
            elif flash_color == "yellow":
                self.blink_yellow()
            elif flash_color == "off":
                self.blink_off()

            blinked += 1
            self.blink_off()
        print(blinked)

    """
    17 = green, 22 = blue, 27 = red
    """

    def blink_blue(self, interval=0.05):
        GPIO.output(17, 0)
        GPIO.output(27, 0)
        GPIO.output(22, 1)
        time.sleep(interval)
        self.blink_off()

    def blink_red(self, interval=0.05):
        GPIO.output(17, 0)
        GPIO.output(27, 1)
        GPIO.output(22, 0)
        time.sleep(interval)
        self.blink_off()

    def blink_yellow(self, interval=0.05):
        GPIO.output(17, 1)
        GPIO.output(27, 1)
        GPIO.output(22, 0)
        time.sleep(interval)
        self.blink_off()

    def blink_green(self, interval=0.05):
        GPIO.output(17, 1)
        GPIO.output(27, 0)
        GPIO.output(22, 0)
        time.sleep(interval)
        self.blink_off()

    def blink_white(self, interval=0.05):
        GPIO.output(17, 1)
        GPIO.output(27, 1)
        GPIO.output(22, 1)
        time.sleep(interval)
        self.blink_off()

    def blink_purple(self, interval=0.05):
        GPIO.output(17, 0)
        GPIO.output(27, 1)
        GPIO.output(22, 1)
        time.sleep(interval)
        self.blink_off()

    def blink_teal(self, interval=0.05):
        GPIO.output(17, 1)
        GPIO.output(27, 0)
        GPIO.output(22, 1)
        time.sleep(interval)
        self.blink_off()

    def blink_off(self):
        GPIO.output(17, 0)
        GPIO.output(27, 0)
        GPIO.output(22, 0)


if __name__ == '__main__':
    BlinkControl().blink(base_color="off", flash_color="yellow", count=100, interval=0.05)
