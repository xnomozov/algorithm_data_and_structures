def linear_search(list_n, target):
    for i in range(len(list_n)):
        if list_n[i] == target:
            return i
    return None


list_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = linear_search(list_n, 3)
print(index)


def verify(index):
    if index is not None:
        print(f'the index is {index}')
    else:
        print('Number is not found')


verify(index)


def binary_search(list_n, target):
    low, high = 0, len(list_n) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == list_n[mid]:
            return mid
        elif target < list_n[mid]:
            high = mid - 1
        elif target > list_n[mid]:
            low = mid + 1


def verify(index):
    if index is not None:
        print(f'the index is {index}')
    else:
        print('Number is not found')


verify(index)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('the stack is empty')
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack after pushing:", stack)

print("Peek:", stack.peek())  # Output: 3
print("Pop:", stack.pop())  # Output: 3
print("Stack after popping:", stack)
print("Is stack empty?", stack.is_empty())  # Output: False

stack.pop()
stack.pop()
print("Is stack empty after popping all elements?", stack.is_empty())


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue after enqueuing:", queue)

print("Peek:", queue.peek())  # Output: 1
print("Dequeue:", queue.dequeue())  # Output: 1
print("Queue after dequeuing:", queue)
print("Is queue empty?", queue.is_empty())  # Output: False

queue.dequeue()
queue.dequeue()
print("Is queue empty after dequeuing all elements?", queue.is_empty())


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current = self.head
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current is None:
            return
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
ll.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None

ll.delete(2)
ll.print_list()  # Output: 0 -> 1 -> 3 -> None

print("Search for 1:", ll.search(1))  # Output: True
print("Search for 4:", ll.search(4))  # Output: False
