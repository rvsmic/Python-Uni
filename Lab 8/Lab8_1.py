import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

lines = ax.plot([],[],"ro")
point = lines[0]

def animate(frame):
    x = 8*np.sin(frame/100)
    y = 8*np.cos(frame/100)
    point.set_data([x],[y])
    return point

#(co jest obrazkiem na animacje, funkcja wywolywana do aktualizacji, okreslenie frames, interval to czas miedzy klatkami)
animation = FuncAnimation(fig,animate,frames=314, interval=50) 
plt.show()