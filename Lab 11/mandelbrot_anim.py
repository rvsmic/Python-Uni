import numpy as np
from time import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.arange(-2,1.01,0.01)
y = np.arange(-1.5,1.51,0.01)
x,y = np.meshgrid(x,y)
z = x + 1j * y
s = z.shape

fig = plt.figure()

z0 = np.copy(z)
res = 255 * np.ones(s)
w = plt.imshow(res,vmin = 0,vmax = 255,cmap = 'binary')

def anim(i):
    global z
    res[np.abs(z)>2] = i
    z = (res == 255) * (z**2+z0)
    w.set_array(res)
    
a = FuncAnimation(fig,anim,frames = 256,interval = 80, repeat = False)

plt.show()