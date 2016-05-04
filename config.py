import socket


REDDIS_CONN = "192.168.111.50"
DB = 'log.sqlite3'
RMQ_HOST = "192.168.111.50"
RMQ_PORT = 5672
RMQ_USER = 'rabbit'
RMQ_PASS = 'bunnyrabbit!!'
MESSAGE_QUEUE = 'nightlyscriptmockup'

PUBSUB_NAME = 'BlinkBlock'

if socket.gethostname() == "vacojaro":
    LOG_LOCATION = "pihole.log"
    GRAVITY_LIST = "gravity.list"
else:
    LOG_LOCATION = "/var/log/pihole.log"
    GRAVITY_LIST = "/etc/pihole/gravity\\.list"
