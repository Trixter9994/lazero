import numpy as np
import scipy
import scipy.fftpack
# fuck the fuck! where is the scipy pack?
import matplotlib.pyplot as plt
# t=scipy.linspace(0,1,11)
# a=[-1,1,-1,1,-1,1,-1,1,-1,1,-1,1]
a=[-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1]
b=abs(scipy.fft(a))
# c=np.fft.fftfreq(len(a), t[1]-t[0])
# c=np.fft.fftfreq(b.shape[-1])
# tuple.
c=np.array(list(range(len(a))))
print(b,c)
# fucking shit. how was this done?
plt.plot(c,b)
plt.show()# what the fuck is this?