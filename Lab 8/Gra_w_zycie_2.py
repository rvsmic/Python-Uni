import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n = 100
# "dlugosc" zycia cienia - 1 da standardowa gre w zycie
shadowTime = 5
Z = np.random.rand(n,n)
Z[Z >= 0.5] = shadowTime
Z[Z < 0.5] = 0

# rozne kolory dla generacji = punkt

def anima(data):
    global Z
    newGrid = Z.copy()
    for i in range(n):
        for j in range(n):
            neighboursCount = (Z[i-1:i+2,j-1:j+2] == shadowTime).sum() - (Z[i,j] == shadowTime)
            if Z[i,j] == shadowTime:
                if neighboursCount < 2 or neighboursCount > 3:
                    newGrid[i,j] -= 1
            else:
                if neighboursCount == 3:
                    newGrid[i,j] = shadowTime
                else:
                    newGrid[i,j] -= 1
    mat.set_data(newGrid)
    Z = newGrid
    return mat

fig,ax = plt.subplots()
mat = ax.matshow(Z,cmap="inferno")
ani = FuncAnimation(fig,anima,frames=500,interval=10)
plt.show()