
import queue

q = queue.Queue()

q.put('A')
q.put('B')

print(q.queue)

q.get()
print(q.queue)

q.put('A')
print(q.queue)


