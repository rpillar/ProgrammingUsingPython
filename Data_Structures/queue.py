# A queue is a fundamental data structure used in many areas of computer science and programming. It follows the first-in, 
# first-out (FIFO) principle, meaning items are added to the end of the queue and removed from the front. Queues provide 
# efficient order processing and are commonly implemented using arrays or linked lists.

# a 'Queue' class - implementing a 'enqueue' method (add items to the 'queue') and a 'dequeue' method (remove an item 
# from the queue). Additions to the 'queue' are always made at the 'end' / data is always 'removed' from the queue
# from the beginning.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.items[0]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
  
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q) # <__main__.Queue object at 0x10109eea0>
print(q.size())    # 3
print(q.isEmpty()) # False