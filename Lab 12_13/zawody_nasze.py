import numpy as np
from multiprocess import Process, Queue
from time import time

def comparer(primer1, primer2):
  if not primer1 or not primer2:
    return -1
  else:
    primer2 = primer2[::-1]
    p1_tab = '*' * (len(primer1 + primer2) - 2) + primer1
    p2_tab = '*' * (len(primer1) - 1) + primer2
    align = []
    for i in range(len(primer1 + primer2) - 1):
      common = list(zip(p1_tab[i:], p2_tab))
      align.append(
        common.count(("A", "T")) + common.count(("T", "A")) +
        common.count(("C", "G")) + common.count(("G", "C"))
        )
    return max(align)
  
def comparer_v2(primer1,primer2,q):
  if not primer1 or not primer2:
    q.put(-1)
  else:
    primer2 = primer2[::-1]
    p1_tab = '*' * (len(primer1 + primer2) - 2) + primer1
    p2_tab = '*' * (len(primer1) - 1) + primer2
    align = []
    for i in range(len(primer1 + primer2) - 1):
      common = list(zip(p1_tab[i:], p2_tab))
      align.append(
        common.count(("A", "T")) + common.count(("T", "A")) +
        common.count(("C", "G")) + common.count(("G", "C"))
        )
    q.put(max(align))

file1 = open('primers.txt', 'r')
lines = file1.readlines()
lines = list(map(lambda x: x.strip(),lines))
counter = 0

t = time()
q = Queue()
n = 12

for i in range(0,len(lines)//n):
  l = [Process(target=comparer_v2,args=(lines[0],lines[i:(i+1)*n],q))].start()

while not q.Empty:
  counter += q.get()

print(counter)
print(time() - t)