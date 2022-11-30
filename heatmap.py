import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
x=np.arange(15**2).reshape((15,15))
sns.heatmap(x,linewidth=0.5,cmap="Dark2")
plt.title("heat map")
plt.show()
