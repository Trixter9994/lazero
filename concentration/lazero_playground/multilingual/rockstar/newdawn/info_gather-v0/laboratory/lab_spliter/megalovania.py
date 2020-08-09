import numpy
import talib

close = numpy.random.random(100)

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
