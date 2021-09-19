"""
LIFO = Last In First Out
1 - 2 - 3 - 4 - 5 = 5 acabe de entrar, es el primero que debe salir 
push, pop, head
"""


class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def pop(self):
        current = self.head
        if(current.next == None):
            number = self.head.data
            self.head = current.next
            current = None
            return

        while(current):
            if(current.next == None):
                print('Elemento a eliminar:', current.data)
                number = current.data
                break
            prev = current
            current = current.next
            # print(prev.data)

        if(current == None):
            print("La pila esta vacia D:")
            return

        prev.next = current.next
        current = current.next
        prev = None

        return number

    def getTop(self):
        if(self.head):
            print("El elemento tope es:", self.head.data)
        else:
            print("Lo sentimos, no tienes datos")
        return

    def printStacks(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next


pila = Stack()
pila.push(5)
pila.push(2)
pila.push(1)
pila.push(7)
pila.push(10)
pila.printStacks()
pila.find(1)
