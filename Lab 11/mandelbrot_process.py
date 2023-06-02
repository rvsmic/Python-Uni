import numpy as np
from time import time
import matplotlib.pyplot as plt
from multiprocess import Process, Queue

x = np.arange(-2,1.01,0.01)
y = np.arange(-1.5,1.51,0.01)
x,y = np.meshgrid(x,y)
z = x + 1j * y
s = z.shape

def mand(z,q,num):
    t = time()
    z0 = np.copy(z)
    s = z.shape
    res = 255 * np.ones(s)
    for i in range(255):
        res[np.abs(z)>2] = i
        z = z**2 + z0
    print("funkcja: ",time()-t)
    q.put((num,res))

q = Queue()
t = time()
n = 4
l = [z[:,i*s[1]//n : (i+1)*s[1]//n] for i in range(n)]
l = [Process(target=mand,args=(l[i],q,i)) for i in range(len(l))]

t = time()
for i in l:
    i.start()
  
# dodatek do poprawnej kolejnosci na wyjsciu
outs = [q.get() for _ in range(n)]
res = np.hstack(list(map(lambda x: x[1],sorted(outs))))

print("Program: ",time()-t)

plt.matshow(res,cmap="binary")
plt.show()