from config import *
from RedisHelper import RedisHelper
import time


total = 0
sub_name = "BlinkBlock"

message_demo = {"flash_color": "red",
                "base_color": "blue",
                "count": 50,
                "interval": 0.1}


if __name__ == '__main__':

    r = RedisHelper()
    r.publish(sub_name, message_demo)
