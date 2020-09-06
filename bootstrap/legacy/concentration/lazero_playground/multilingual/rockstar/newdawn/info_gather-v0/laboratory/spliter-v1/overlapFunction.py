import talib, numpy
# finance functions are the best.
def wrap(_list):
    close = numpy.array(list(map((lambda x : float(x)),_list)))
    return close
# this is taichi.
hotpot={}
mississippi=""
with open("README","r") as fortnight:
    mississippi=fortnight.read()
    hotpot=set(mississippi)
print(hotpot)
# use ascii values!
# this is one of our main purpose here!
# i may vomit.
# fuck me! just get the fucking research out!
# not inside those common patterns.
hotspot=list(filter((lambda x:not ((ord(x)>=97 and ord(x)<=122 )or (ord(x)>=65 and ord(x)<=90)) ),hotpot ) )
# derandom
print(hotspot)
# you didn't add numbers to it.
# i need my spliter!
# you can also consider the lone-wolf filter.
# filter out those things that shall always appear in a group.
# this can be achieved by adding some attributes to each letter.
# LOCAL! LOCAL! LOCAL!

# the second step is to get the basic information: linear index.
# create the thing?
#nothing=list(enumerate(hotspot))
# you must be a list.
#print(nothing)
nothing=[]
for k in range(len(hotspot)):
    nothing.append([])

for r,k in enumerate(list(mississippi)):
    if k in hotspot:
#        print (r,k)
        # and append the shit.
        # consider some linear algorithm?
        # you want to use finance method to do this task? perfect. MACD, PSY, KDJ and more.
        nothing[hotspot.index(k)].append(r)

    # the r is the index.

# i cannot say no word.
# use double derivative instead.
derivative=(lambda k0: [(k0[m+1]-k0[m]) for m in range(len(k0)-1)])
# to illustrate this:
for r,k in enumerate(nothing):
    print(r,k)
    vm=wrap(k)
    upperband, middleband, lowerband = talib.BBANDS(vm, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    print(upperband,middleband,lowerband)
    print("-----jigsaw-----")
    print(list(talib.WMA(vm, timeperiod=30)))
    print(list(talib.TRIMA(vm, timeperiod=30)))
    print(list(talib.TEMA(vm, timeperiod=30)))
    print(list(talib.T3(vm, timeperiod=5, vfactor=0)))
    print(list(talib.SMA(vm, timeperiod=30)))
    print(list(talib.MIDPOINT(vm, timeperiod=14)))
#    print(list(talib.MAMA(vm, fastlimit=0, slowlimit=0)))
    print(list(talib.MA(vm, timeperiod=30, matype=0)))
    print(list(talib.KAMA(vm, timeperiod=30)))
    print(list(talib.HT_TRENDLINE(vm)))
    # you have the trend here?
    print(list(talib.EMA(vm, timeperiod=30)))
    print(list(talib.DEMA(vm, timeperiod=30)))
    # reading is like a survey, so as the stock market.
    if len(k)>3:
        # we have got some variable periods here, how do we see this?
        # only if we can conclude.
        high0=derivative(k)
        high=wrap(high0[:-1])
        low=wrap(derivative(high0))
        print(list(talib.SAREXT(high,low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)))
        print(list(talib.SAR(high, low, acceleration=0, maximum=0)))
        print(list(talib.MIDPRICE(high, low, timeperiod=14)))
        # put it all over here.
        # i use finance functions to shoot your head off!
    else:
        pass
