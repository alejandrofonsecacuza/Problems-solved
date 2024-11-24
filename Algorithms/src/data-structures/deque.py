from collections import deque
d=deque()
for i in range(10):
    d.append(i)

d.appendleft(1000)

d.remove(3)
print(d.index(5))