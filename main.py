#ex1

import numpy as np
import matplotlib.pyplot as plt

s1 = 0.9
s2 = 0.7
n0 = 0
dN = 20
Nk = 2000

t = np.arange(n0, Nk, dN)
a1 = t/(t * s1 + 1 - s1)
a2 = t/(t * s2 + 1 - s2)

plt.plot(t, a1)
plt.plot(t, a2)
plt.show()