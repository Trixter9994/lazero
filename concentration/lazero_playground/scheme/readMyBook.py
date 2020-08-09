# select few things.
# not to read those readed ones.
# recall-the-next test?
# never forget? i force you to forget.
# how to start autonomous learning instead of being a spider, a mocking machine?
# i do not know how to define authentic.
# randomly access ip address! how fucking insane?
# i cannot do this, so computer will do?
import random
import requests
# not to hit my local addresses.


def nowFail(b):
  with open("collective_ip.log","a+") as f:
    f.write(b+"\n")

def randomIp():
  r = list(range(1, 255))
  r0 = ".".join([str(random.choice(r)) for x in range(4)])
  return r0

while True:
  s = randomIp()
  # print(s)
  try:
    r = requests.get("http://" + s,timeout=2)
    nowFail(s)
    # just put it into the pocket.
    # print(r.content)
  except:
    pass
    # print("NOTHING HERE.")
# what the fuck?
# timeout?
# what the fuck is internet?
# why we have got nothing in the air?
# what is the probability of finding a website?
# is it a seizure?
# man what the fuck is going on?
# is it really that hard to find one active site?
# or port?
# i will vomit.