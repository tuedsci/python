# RANDOM SAMPLING

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# --------------------------------------------------
# NORMAL DISTRIBUTION
# --------------------------------------------------

# %% Heights of 10k people drawn from N(1.7, 0.5**2)
heights = np.random.normal(loc=1.7, scale=0.5, size=10000)
plt.hist(heights, bins=20)
plt.show()
