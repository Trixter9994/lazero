import numpy as np
import scipy.stats as stats
# excuse me where is the data?
data = np.loadtxt('data.csv', delimiter=',', dtype=int, skiprows=1)

for col in range(1, len(data[0])):
    tau, p = stats.kendalltau(data[:,0], data[:,col])
    print ("column %2d: tau = %+g, p = %g" % (col, tau, p))

for order in ('C', 'F'):
    flat = data[:,1:].flatten(order)
    tau, p = stats.kendalltau(flat, np.arange(len(flat)))
    print ("full data (%s): tau = %+g, p = %g" % (order, tau, p))
