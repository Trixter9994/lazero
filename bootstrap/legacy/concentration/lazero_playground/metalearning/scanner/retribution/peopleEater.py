import scipy
import matplotlib.pyplot as plt
import numpy as np
from scipy import pi
t = scipy.linspace(0,120,4000)
acc = lambda t: 10*scipy.sin(2*pi*2.0*t) + 5*scipy.sin(2*pi*8.0*t) + 2*scipy.random.random(len(t))

signal = acc(t)

FFT = abs(scipy.fft(signal))
FFT = np.fft.fftshift(FFT)
freqs = np.fft.fftfreq(signal.size)
print(freqs)
plt.plot(freqs,FFT,'x')
plt.show()