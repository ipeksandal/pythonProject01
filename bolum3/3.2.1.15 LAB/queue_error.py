class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.elements = []

    def put(self, elem):
        self.elements.append(elem)

    def get(self):
        if len(self.elements) == 0:
            raise QueueError("Queue is empty. Cannot get from empty queue.")
        return self.elements.pop(0)


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError as e:
    print("Queue error:", e)
