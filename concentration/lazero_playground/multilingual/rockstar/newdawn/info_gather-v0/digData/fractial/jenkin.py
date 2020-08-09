import numpy as np
#from timeit import timeit
def mandelbrot(z,maxiter):
    c = z
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return maxiter

def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    sob=[]
    nuke=""
    for r in r1:
        for i in r2:
            nuke=mandelbrot(complex(r, i),maxiter)
            print(nuke)
            sob.append(nuke)
    return (r1,r2,sob)

#timeit((lambda: mandelbrot_set(-2.0,0.5,-1.25,1.25,1000,1000,80) ),number=10000)

print(mandelbrot_set(-2.0,0.5,-1.25,1.25,1000,1000,80))
#print("-----spliter-----")

#timeit((lambda:mandelbrot_set(-0.74877,-0.74872,0.06505,0.06510,1000,1000,2048)),number=10000)
