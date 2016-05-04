from subprocess import check_output
from config import *
import time
import datetime
from RedisHelper import RedisHelper


class PiHole:
    _redis = RedisHelper()

    def __init__(self):
        self.last_count = 0
        self.day = datetime.datetime.today().weekday()

    def calc_blocked_today(self):
        output = check_output("/bin/cat " + LOG_LOCATION + " | /usr/bin/awk '/" +
                              GRAVITY_LIST + "/ && !/address/ {print $6}' | wc -l", shell=True)
        return int(output)

    def calc_queries_today(self):
        stuff = check_output("/bin/cat " + LOG_LOCATION +
                             " | /usr/bin/awk '/query/ {print $6}' | wc -l", shell=True)
        return int(stuff)

    def calc_blocklist_count(self):
        output = check_output(
            "wc -l " + GRAVITY_LIST + " | awk '{print $1}'", shell=True)
        return int(x=output)

    def calc_perc_blocked(self):
        return (self.calc_blocked_today() / self.calc_queries_today()) * 100

    def monitor(self):
        while True:
            if not self.day == datetime.datetime.today().weekday():
                self.day = datetime.datetime.today().weekday()
                self.last_count = 0
            else:
                cur_count = self.calc_blocked_today()
                if cur_count > self.last_count:
                    message = {
                        "count": cur_count - self.last_count,
                        "interval": .05,
                        "flash_color": "red",
                        "base_color": "white"
                    }
                    self.last_count = cur_count
                    self._redis.publish(PUBSUB_NAME, message)
                    print(message)

            time.sleep(5)


if __name__ == '__main__':
    p = PiHole()
    p.monitor()
