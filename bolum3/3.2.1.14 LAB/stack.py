class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop from empty stack.")
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

    def is_empty(self):
        return len(self.__stk) == 0


class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def get_counter(self):
        return self.counter

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop from empty stack.")
        val = super().pop()
        self.counter += 1
        return val


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter()) 
