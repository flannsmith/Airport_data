import queue

q = queue.Queue()


#FIFO implementation of queue
for i in range(5):
   q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()


#LIFO
q = queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()
