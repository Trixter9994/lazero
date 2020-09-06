import numpy
import talib

_list=[0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1]
# real to double
close = numpy.array(list(map((lambda x : float(x)),_list)))

print(close)

print("-----spliter-----")

print(type(close))

output0 = talib.SMA(close)

from talib import MA_Type

upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)

# I really don't know what is going on.

output = talib.MOM(close, timeperiod=5)

# fuck me okay???

print(output0)
print(type(output0))
print("-----spliter-----")
print(output)
print(type(output))

output1=talib.MAMA(close)
# you better check the wrapper first.
print("-----spliter-----")
print(output1)
