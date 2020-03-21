import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

Z = np.array([[1, 1, 1], [1, -10, 1], [1, 1, 1]])
print(Z)
fig, ax0 = plt.subplots(1, 1)
c = ax0.pcolor(Z, edgecolors='k', linewidths=4)
ax0.set_title('default: no edges')
plt.show()
