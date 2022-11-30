import numpy as np
import matplotlib.pyplot as plt
x=np.arange(100).reshape((10,10))
plt.pcolormesh(x,cmap="coolwarm")
plt.show()
