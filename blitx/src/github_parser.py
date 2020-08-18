# get the thing.
# from bs4 import BeautifulSoup
import requests
import re
import copy
from storeADill import storeAList

init=[]
listString = ["artificial", "life"]
little = "+".join(listString)
formatString = "https://github.com/search?q={}".format(little)

r = requests.get(formatString)
res = r.text
init.append(copy.copy(res))

def dnf(x):
    if len(x) > 0:
        return x[0]
    else:
        return None


# print(res,type(res))
# get largest number.
# html = BeautifulSoup(res,features='lxml')
# "/search?p=3&amp;q=artificial+life&amp;type=Repositories"
target = list(filter(lambda x: little in x,
                     re.findall(r"/search\?p=\d+[^\"]+", res)))

target = list(
    map(lambda x: dnf(re.findall(r"[0-9]+", x)), target))
target = list(map(lambda x: int(x), list(
    filter(lambda x: x is not None, target))))

# for x in target:
#     print(x)
# target = list(map(lambda x: dnf(re.findall(r"\d+", x)),
#                   list(filter(lambda x: x is not None, target))))
# # # for x in target:
# #     print(x)
max=sorted(target)[-1]

for x in range(max):
    y=x+1
    s="/search?p={}&amp;q={}&amp;type=Repositories".format(y,little)
    r=requests.get("https://github.com"+s)
    req=r.text
    init.append(copy.copy(req))

stoteAList(init)
