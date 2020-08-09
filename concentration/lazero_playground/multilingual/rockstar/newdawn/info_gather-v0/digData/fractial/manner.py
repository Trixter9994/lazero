from numba import jit
import numpy as np
from timeit import timeit

@jit
def mandelbrot(creal,cimag,maxiter):
    real = creal
    imag = cimag
    for n in range(maxiter):
        real2 = real*real
        imag2 = imag*imag
        if real2 + imag2 > 4.0:
            return n
        imag = 2* real*imag + cimag
        real = real2 - imag2 + creal       
    return 0


@jit
def mandelbrot_set4(xmin,xmax,ymin,ymax,width,height,maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))
    for i in range(width):
        for j in range(height):
            n3[i,j] = mandelbrot(r1[i],r2[j],maxiter)
    return (r1,r2,n3)

timeit((lambda: mandelbrot_set4(-2.0,0.5,-1.25,1.25,1000,1000,80)),number=100)

print("-----spliter-----")

timeit((lambda: mandelbrot_set4(-0.74877,-0.74872,0.06505,0.06510,1000,1000,2048)),number=100)
