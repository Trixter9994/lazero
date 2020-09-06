from getFromDill import returnAList
import random
#from pairail import send_string as send_message
from darkmart import broadcast as send_message

def reader(f):
    with open(f,"r") as f0:
        return f0.read()

r=returnAList()
while True:
    try:
        r0=random.choice(r)
        r1=reader(r0)
        send_message(r1)
    except:
        pass
#print(r)
