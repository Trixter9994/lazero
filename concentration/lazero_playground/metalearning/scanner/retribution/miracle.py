# hello world!
import numpy as np
import matplotlib.pyplot as plt
# directly use the fft func?
# useless prick!
n=np.array([0,1,0,1,0,1,0,1,0,1,0,1,0,1])
n1=np.array([0,1,2,0,1,2,0,1,2,0,1,2])
n0=np.array([0,1,2,0,1,2,0,1,2,0,1,2,0,1,0,1,0,1,0,1,0,1,0,1,0,1])
f=np.fft.fft(n)
# print(f)
# f0=np.fft.fft(n1)
# f1=np.fft.fft(n0)
# # what is this hell?
# print(f)
# print(f0)
# print(f1)
t = np.arange(256)
# print(t)
g= np.sin(t)
# print(g)
# they will be fucked. ALL OF THEM.
s0=[n,n0,n1]
for s in s0:
    sp = np.fft.fft(s)
    freq = np.fft.fftfreq(s.shape[-1])
    print(freq)
    # what is this frequency?
    plt.plot(freq, sp.real, freq, sp.imag)
    plt.show()
    # kill them all.