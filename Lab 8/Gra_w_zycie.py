import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n = 150
Z = np.random.rand(n,n)
Z[Z>=0.5] = 1
Z[Z<0.5] = 0

# rozne kolory dla generacji = punkt

def anima(data):
    global Z
    newGrid = Z.copy()
    for i in range(n):
        for j in range(n):
            # neighboursCount = (Z[i, (j-1)%n] + Z[i, (j+1)%n] + Z[(i-1)%n, j] + Z[(i+1)%n, j] + Z[(i-1)%n, (j-1)%n] + Z[(i-1)%n, (j+1)%n] + Z[(i+1)%n, (j-1)%n] + Z[(i+1)%n, (j+1)%n])
            neighboursCount = Z[i-1:i+2,j-1:j+2].sum() - Z[i,j]
            if Z[i,j] == 1:
                if(neighboursCount < 2) or (neighboursCount > 3):
                    newGrid[i,j] = 0
            else:
                if neighboursCount == 3:
                    newGrid[i,j] = 1
    mat.set_data(newGrid)
    Z = newGrid
    return [mat]

fig,ax = plt.subplots()
mat = ax.matshow(Z,cmap="cividis")
ani = FuncAnimation(fig,anima,frames=2000,interval=10)
plt.show()