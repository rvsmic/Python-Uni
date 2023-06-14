from time import time
from multiprocessing import cpu_count
from multiprocess import Process, Queue

def comparer(primer1, primer2):
  if not primer1 or not primer2:
    return -1
  else:
    n = len(primer1)
    # nw czemu to musi byc
    primer2 = primer2[::-1]
    align = []
    for i in range(1,n+1):
      # P1 - - - - A B C D E
      # P2 A B C D E - - - -
      common = list(zip(primer1[:i],primer2[n-i:]))
      align.append(
                common.count(("A", "T")) + common.count(("T", "A")) +
                common.count(("C", "G")) + common.count(("G", "C"))
            )
    for i in range(1,n):
      # P1 A B C D E -
      # P2 - A B C D E
      common = list(zip(primer1[i:],primer2[:n-i]))
      align.append(
                common.count(("A", "T")) + common.count(("T", "A")) +
                common.count(("C", "G")) + common.count(("G", "C"))
            )
    return max(align)

def multi_comparer(primer1,primers_arr,q):
  counter = 0
  for pr in primers_arr:
    counter += comparer(primer1,pr)
  q.put(counter)

file1 = open('primers.txt', 'r')
lines = file1.readlines()
lines = list(map(lambda x: x.strip(),lines))
counter = 0
t = time()

cpu = cpu_count()
lines_len = len(lines)
q = Queue()

processes = [Process(target=multi_comparer,args=(lines[0],lines[(i*lines_len//cpu):(i+1)*lines_len//cpu],q)).start() for i in range(cpu)]

counter = sum([q.get() for _ in range(cpu)])

print(time() - t)
print(counter)