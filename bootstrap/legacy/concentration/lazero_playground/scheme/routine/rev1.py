import zmq
import sys

lt0 = "127.0.0.7"

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print ("Collecting updates from weather server...")
socket.connect("tcp://"+lt0+":%s" % port)

if len(sys.argv) > 2:
    socket.connect("tcp://"+lt0+":%s" % port1)
# this is shit.
# man i do not know how programs establish connection but this is shit!
# 本地过滤
topicfilter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

# Process 5 updates
total_value = 0
# for update_nbr in range(5):
while True:
  # could be missing?
  # need repair?
  # what to do then?
    string = socket.recv_string()
    topic, messagedata, pub_server_name = string.split()
    total_value += int(messagedata)
    # shit, you even got this shit.
    print (topic, messagedata, pub_server_name)

# print ("Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value / update_nbr))
