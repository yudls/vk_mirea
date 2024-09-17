#ex4

import numpy as np
import matplotlib.pyplot as plt
import math
n1 = 500
n2 = 800
s0 = 0.9
dS = -0.0025
Sk = 0.8

t = np.arange(s0, Sk, dS)
a1 = n1 + (1 - n1) * t
a2 = n2 + (1 - n2) * t

plt.plot(t, a1)
plt.plot(t, a2)
plt.show()