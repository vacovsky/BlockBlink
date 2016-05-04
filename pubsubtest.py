from config import *
from RedisHelper import RedisHelper
import time


total = 0
sub_name = "BlinkBlock"

message_demo = {"flash_color": "blue",
                "base_color": "yellow",
                "count": 500,
                "interval": 0.02}


if __name__ == '__main__':

    r = RedisHelper()
    r.publish(sub_name, message_demo)
