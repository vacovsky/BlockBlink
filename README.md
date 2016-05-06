#blockblink#

This was created one evening because I wanted a snazzy way to blink the multicolor LED connected to my Pi via GPio.  I use it to monitor various events on my network from random scripts, but primarily use it to see when ads are blocked, and as a visual way to monitor the status of various internal network services.

#Setup#

1. Install Redis server locally or otherwise.
2. Add the Redis server IP to the config.py file.
3. Run ```python3 PiHole.py``` on the device hosting PiHole
4. On the device with the LED connected, run ```python3 Main.py``` (may require permission elevation).
5. To add any other event blinks (different colors, intervals, counts, etc), just publish to the same PubSub as is specified in ```config.py```, where Main.py listens.

##PubSub message format
The message format for the PubSub is a python dictionary (it looks like Json, but isn't serialized on the publisher side).  Example can be found in pubsubtest.py, or below:

```
from config import *
from RedisHelper import RedisHelper

total = 0
sub_name = "BlinkBlock"

message_demo = {"flash_color": "red",
                "base_color": "off",
                "count": 5,
                "interval": 0.1}

if __name__ == '__main__':
    r = RedisHelper()
    r.publish(sub_name, message_demo)

```