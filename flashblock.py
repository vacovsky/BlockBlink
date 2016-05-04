import requests
from config import *
from RedisHelper import RedisHelper


url = "http://192.168.111.126/admin/blinker.php"

print(requests.get(url, params=None).text)


while __name__ == '__main__':
    r = RedisHelper()
    r.subscribe('BlinkBlock')
    for message in r.PubSub.listen():
        print(message)
