#ex3

import numpy as np
import matplotlib.pyplot as plt
import math
s1 = 0.9
s2 = 0.7
n0 = 10
dN = 20
Nk = 2000

t = np.arange(n0, Nk, dN)
a1 = t + (1 - t) * s1
a2 = t + (1 - t) * s2

plt.plot(t, a1)
plt.plot(t, a2)
plt.show()