from RedisHelper import RedisHelper
from BlinkControl import BlinkControl
import json
from config import *


class Main:
    redis = RedisHelper()
    blinker = BlinkControl()

    def __init_(self):
        pass

    def listen(self):
        self.redis.subscribe(PUBSUB_NAME)
        for message in self.redis.PubSub.listen():
            print("%s" % message)
            data = message["data"]
            if data == 1:
                continue
            datastr = data.decode('utf8').replace("'", '"')
            datadict = json.loads(datastr)

            self.blinker.blink(
                base_color=datadict["base_color"],
                flash_color=datadict["flash_color"],
                count=datadict["count"],
                interval=datadict["interval"])


if __name__ == '__main__':
    print("Starting LED listener for PUBSUB: %s." % PUBSUB_NAME)
    Main().listen()
