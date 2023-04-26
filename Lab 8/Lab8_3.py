import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# n = 100
# X,Y = np.meshgrid(np.linspace(-n,n,100),np.linspace(-n,n,100))
# Z = 80**2 - ((X-50)**2 + (Y-50)**2)

# n = 2
# X,Y = np.meshgrid(np.linspace(-n,n,100),np.linspace(-n,n,100))
# Z = np.sin(X*2) + np.cos(Y*3*np.sin(X))

# plt.matshow(Z, cmap="plasma")
# plt.show()

grid_size = 200
X,Y = np.meshgrid(np.linspace(-np.pi/2,np.pi/2,grid_size),np.linspace(-np.pi/2,np.pi/2,grid_size))
# Z = np.zeros((grid_size,grid_size))
Z = np.sin(X)*np.cos(Y)

def anima(frame,X,Y,Z):
    Z = np.sin(X+np.sin(frame/10)) * np.cos(Y-np.sin(frame/20)) + np.sin(X+Y) * np.cos(frame/10)
    mat.set_data(Z)
    return mat

fig,ax = plt.subplots()
mat = ax.matshow(Z,cmap="plasma")
ani = FuncAnimation(fig,anima,frames=200,fargs=(X,Y,Z),interval=1)
plt.show()
