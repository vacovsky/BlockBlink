from config import *
from RedisHelper import RedisHelper


total = 0
sub_name = "BlinkBlock"

message_demo = {"flash_color": "red",
                "base_color": "purple",
                "count": 50,
                "interval": 0.04}


if __name__ == '__main__':

    r = RedisHelper()
    r.publish(sub_name, message_demo)
