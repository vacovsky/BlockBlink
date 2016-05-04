from config import *
from redismanager import RedisHelper
import time


total = 0
sub_name = "BlinkBlock"

message_demo = {"flash_color": "red",
                "base_color": "blue",
                "count": 44,
                "interval": 0.01}


while __name__ == '__main__':

    r = RedisHelper()
    r.publish(sub_name, message_demo)
    time.sleep(5)
