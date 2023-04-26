import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x,y = 0,0


scat = ax.scatter(x,y)

def init():
    ax.set_xlim(0,2*np.pi)
    ax.set_ylim(-1,1)

def update(frame):
    x = frame
    y = np.sin(frame)
    scat.set_offsets([x,y])

 #(co jest obrazkiem na animacje, funkcja wywolywana do aktualizacji, ilosc klatek, interval to czas miedzy klatkami)
animation = FuncAnimation(fig,update,frames=np.linspace(0,2*np.pi,120),init_func = init,interval = 10)
plt.show()