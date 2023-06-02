import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

d = 1000
x = np.linspace(-1.5,1.5,d)
y = np.linspace(-1.5,1.5,d)
x,y = np.meshgrid(x,y)
z = x + 1j * y
s = z.shape

c = -0.8+ 0.156j

fig = plt.figure()

z0 = np.copy(z)
res = 255 * np.ones(s)
w = plt.imshow(res,vmin = 0,vmax = 255,cmap = 'plasma')

def anim(i):
    global z
    res[np.abs(z)>2] = i
    z = (res == 255) * (z*z+c)
    w.set_array(res)
    
a = FuncAnimation(fig,anim,frames = 256,interval = 40, repeat = False)

plt.show()