from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, step):
        self.queue.append(step)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()

    def rear(self):
        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return

    def front(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return