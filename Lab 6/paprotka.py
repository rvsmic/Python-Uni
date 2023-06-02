import random
import matplotlib.pyplot as plt

x = 0
y = 0
x_arr = []
y_arr = []

for i in range(50000):
    l = random.choices([1,2,3,4], weights = (85,7,7,1))[0]
    if l == 1:
        x,y = 0.85*x + 0.04*y,-0.04*x + 0.85*y + 1.6
    elif l==2:
        x,y = -0.15*x + 0.28*y,0.26*x + 0.24*y + 0.44
    elif l==3:
        x,y = 0.20*x - 0.26*y,0.23*x + 0.22*y + 1.6
    else:
        x,y = 0,0.16*y
    x_arr.append(x)
    y_arr.append(y)

plt.scatter([x for x in x_arr],[y for y in y_arr], s=0.2, edgecolor='green')
plt.show()