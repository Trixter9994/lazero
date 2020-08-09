from utl import get_publisher
import time
g = get_publisher("127.0.0.7", "3000")

while True:
    g0 = g.send_string("hello world")
    print(time.time())
#    print(g0)
