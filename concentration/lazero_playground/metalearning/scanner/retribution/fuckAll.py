import matplotlib.pyplot as plt
import numpy as np
a=(lambda x: np.array(x))
b=[[1,2,3],[4,5,6]]
plt.plot(a(b[0]),a(b[1]),a(b[1]),a(b[0]))
# two fucking lines.
plt.show()
# fuck you fourier!