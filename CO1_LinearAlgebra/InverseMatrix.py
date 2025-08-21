# Inverse of a matrix
# importing packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
# %pylab inline  # Remove or comment out this Jupyter magic if running as a script
plt.rcParams['figure.figsize'] = (4,4)
np.set_printoptions(suppress=True)

A = np.array([[3, 0, 2], [2, 0, -2], [0, 1, 1]])
A_inv = np.linalg.inv(A)
print(A_inv)

