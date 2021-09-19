"""
FIFO = Firts In First Out
1, 2, 3, 4, 5, 6, 7, 8
First = 1
Last = 8
list, dequeu, append
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, data):
        newNode = Node(data)
        if(self.first):
            current = self.first
            while(current.next):
                current = current.next
            current.next = newNode
            self.last = newNode
        else:
            self.first = newNode
            self.last = newNode

    def dequeue(self):
        if(self.first):
            prev = self.first
            current = prev.next
            self.first = current
            print('Elemento a eliminar:', prev.data)
            number = prev.data
            prev = None
            return number
        else:
            return

    def getFirst(self):
        if(self.first):
            return self.first.data
        else:
            return None

    def getLast(self):
        return self.last.data

    def reverseQueue(self):
        prev = None
        current = self.first
        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next
            self.last = current
        self.first = prev
        return

    def printAllQueue(self):
        current = self.first
        while(current):
            print(current.data, sep=" ")
            current = current.next


def getSum(cola):
    total = 0
    while(cola.getFirst() != None):
        number = cola.dequeue()
        total = total + number
    return total


colas = Queue()
colas.enqueue(1)
colas.enqueue(2)
colas.enqueue(3)
colas.printAllQueue()
print(getSum(colas))
""" print("Cola Inversa")
colas.reverseQueue()
colas.printAllQueue() """
