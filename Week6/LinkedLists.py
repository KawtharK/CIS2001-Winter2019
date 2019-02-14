class Node:

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)

class LinkedList:

    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.number_of_nodes = 0

    def is_empty(self):
        return self.first_node == None

    def append(self, data):
        if self.first_node is None:
            self.first_node = Node(data)
            self.last_node = self.first_node
        else:
            new_node = Node(data)
            self.last_node.next_node = new_node
            self.last_node = new_node
        self.number_of_nodes += 1

    def add_to_front(self, data):
        new_front = Node(data, self.first_node)
        self.first_node = new_front

        if self.last_node is None:
            self.last_node = self.first_node

    def dequeue(self):
        self.check_is_empty()

        value = self.first_node.data
        if self.first_node == self.last_node:
            self.last_node = None
        self.first_node = self.first_node.next_node

        return value

    def pop(self):
        self.check_is_empty()

        self.number_of_nodes -= 1

        if self.first_node == self.last_node:
            value = self.first_node.data
            self.first_node = None
            self.last_node = None
            return value

        current_node = self.first_node

        while current_node.next_node != self.last_node:
            current_node = current_node.next_node

        value = self.last_node.data
        self.last_node = current_node
        self.last_node.next_node = None
        return value

    def check_is_empty(self):
        if self.is_empty():
            raise IndexError("Linked List is empty")

    def __str__(self):
        result = "["
        current_node = self.first_node
        while current_node != None:
            result += str(current_node)
            current_node = current_node.next_node
            if current_node != None:
                result += ", "
        result += "]"
        return result


eric = Node("Eric")
patrick = Node("Patrick")
talia = Node("Talia")

eric.next_node = patrick
patrick.next_node = talia

current_node = eric

while(current_node != None):
    print(current_node)
    current_node = current_node.next_node



linkedList = LinkedList()
linkedList.append("Eric")
linkedList.append("Patrick")
linkedList.append("Talia")
print(linkedList)