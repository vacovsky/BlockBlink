from subprocess import check_output
from config import *


class PiHole:

    def calc_blocked_today(self):
        output = check_output("/usr/bin/cat " + LOG_LOCATION + " | /usr/bin/awk '/" +
                              GRAVITY_LIST + "/ && !/address/ {print $6}' | wc -l", shell=True)
        return int(output)

    def calc_queries_today(self):
        stuff = check_output("/usr/bin/cat " + LOG_LOCATION +
                             " | /usr/bin/awk '/query/ {print $6}' | wc -l", shell=True)
        return int(stuff)

    def calc_blocklist_count(self):
        output = check_output(
            "wc -l " + GRAVITY_LIST + " | awk '{print $1}'", shell=True)
        return int(x=output)

    def calc_perc_blocked(self):
        return (self.calc_blocked_today() / self.calc_queries_today()) * 100


if __name__ == '__main__':
    p = PiHole()
    print(p.calc_queries_today())
    print(p.calc_blocked_today())
    print(p.calc_blocklist_count())
    print(p.calc_perc_blocked())
