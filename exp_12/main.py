from my_queue import Queue

q = Queue()

q.push(1)
q.push(2)
q.push(3)       # 123
print(q.pop()) # Output: 1      # 23

q.rotate(1)                     # 32

print(q.pop()) # Output: 3      #2

q.extend([4,5,6])               #2456

print(q.pop()) # Output: 2      #456
