from collections import deque
import parameters.parameters_search as p


class Queue(deque):

    def __init__(self, iterable=[], maxlen=None) -> None:
        super().__init__(iterable=iterable, maxlen=maxlen)
        self.items_added = 0

    def append(self, x):
        super().appendleft(x)
        self.items_added += 1
        if self.items_added % p.COLLECTION_STEP_PRINT == 0:
            print("Items added:", self.items_added)

    def pop(self):
        x = super().pop()
        return x


class Stack(deque):

    def __init__(self, iterable=[], maxlen=None) -> None:
        super().__init__(iterable=iterable, maxlen=maxlen)
        self.items_added = 0

    def append(self, x):
        super().append(x)

        self.items_added += 1
        if self.items_added % p.COLLECTION_STEP_PRINT == 0:
            print("Items added:", self.items_added)

    def pop(self):
        x = super().pop()
        return x


if __name__ == "__main__":
    print("--- Queue ---")
    queue = Queue()
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)
    a = queue.pop()
    print(a)
    a = queue.pop()
    print(a)
    a = queue.pop()
    print(a)
    a = queue.pop()
    print(a)

    print(queue)

    print("--- Stack ---")
    stack = Stack()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)
    a = stack.pop()
    print(a)
    a = stack.pop()
    print(a)
    a = stack.pop()
    print(a)
    a = stack.pop()
    print(a)

    print(stack)
