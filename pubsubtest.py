from config import *
from RedisHelper import RedisHelper
import time


total = 0
sub_name = "BlinkBlock"

message_demo = {"flash_color": "off",
                "base_color": "yellow",
                "count": 5,
                "interval": 0.5}


if __name__ == '__main__':

    r = RedisHelper()
    r.publish(sub_name, message_demo)
