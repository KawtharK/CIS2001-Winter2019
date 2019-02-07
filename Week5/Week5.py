import sys

class MyStack:

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def peek(self):
        if len(self._data) == 0:
            raise IndexError("Stack is empty")
        return self._data[len(self._data)-1]

    def pop(self):
        return self._data.pop()

    def __len__(self):
        return len(self._data)

    def get_size(self):
        return sys.getsizeof(self._data)

class MyQueue:

    def __init__(self):
        self._data = []
        self._number_of_items_in_queue = 0
        self._front_index = None

    def enqueue(self, item):
        if self._front_index is None:
            self._front_index = 0
        self._data.append(item)
        self._number_of_items_in_queue += 1

    def dequeue(self):
        if self._number_of_items_in_queue == 0:
            raise IndexError("Queue is empty")
        value = self._data[self._front_index]
        self._data[self._front_index] = None
        self._number_of_items_in_queue -= 1
        self._front_index += 1
        return value

    def first(self):
        if self._number_of_items_in_queue == 0:
            raise IndexError("Queue is empty")
        return self._data[self._front_index]

    def __len__(self):
        return self._number_of_items_in_queue

    def get_size(self):
        return sys.getsizeof(self._data)

mystack = MyStack()
for number in range(100):
    mystack.push(number)
    print("Current items: {} - size: {}".format(len(mystack), mystack.get_size()))

while len(mystack) > 0:
    mystack.pop()
    print("Current items: {} - size: {}".format(len(mystack), mystack.get_size()))

myqueue = MyQueue()
for number in range(100):
    myqueue.enqueue(number)
    print("Current items: {} - size: {}".format(len(myqueue), myqueue.get_size()))

while len(myqueue) > 0:
    myqueue.dequeue()
    print("Current items: {} - size: {}".format(len(myqueue), myqueue.get_size()))
