#ex2

import numpy as np
import matplotlib.pyplot as plt

n1 = 500
n2 = 800
s0 = 0.9
dS = -0.0025
Sk = 0.8

t = np.arange(s0, Sk, dS)
a1 = n1/(n1 * t + 1 - t)
a2 = n2/(n2 * t + 1 - t)

plt.plot(t, a1)
plt.plot(t, a2)
plt.show()