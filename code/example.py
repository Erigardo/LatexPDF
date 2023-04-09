import numpy as np
import matplotlib.pyplot as plt
import os

fig_dir = os.path.join(os.getcwd(), 'src')

fig = plt.figure(figsize=(3, 3))
plt.plot([2, 3, 9], [1, 2, 4])
plt.tight_layout()
plt.show()
fig.savefig('../src/figure/example.png', dpi=300)
#plt.savefig("../src/figure/example.png")
