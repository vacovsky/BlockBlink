from redismanager import RedisHelper
import json
import sys


class Main:
    redis = RedisHelper()

    def __init_(self):
        self.last_count = get_current_count()

    def listen(self):
        self.redis.subscribe('BlinkBlock')
        for message in self.redis.PubSub.listen():
            data = message["data"]
            if data == 1:
                continue
            datastr = data.decode('utf8').replace("'", '"')
            datadict = json.loads(datastr)
            print(datadict["base_color"])
            print(datadict["flash_color"])
            print(datadict["count"])
            print(datadict["interval"])

            # self.blink(base_color="green", flash_color="red", count=1, interval=0.05)

    
    def check_blocked_counter(self):
        pass
        """global last_count
                                print(last_count)
                                current_count = get_current_count()
                                if current_count > last_count:
                                    print(current_count, ' > ', last_count)
                                    blink_purple(current_count - last_count)
                                    last_count = current_count
                        
                                elif current_count < last_count:
                                    last_count = 0"""


if __name__ == '__main__':
    Main().listen()
