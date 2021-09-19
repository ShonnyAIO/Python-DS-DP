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
            self.head = current.next
            data = current.data
            print('Elemento a eliminar:', data)
            current = None
            return data

        while(current):
            if(current.next == None):
                print('Elemento a eliminar:', current.data)
                data = current.data
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

        return data

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


def valid_parenthesis(pila):
    temp = []
    temp.append(pila.pop())
    temp.append(pila.pop())
    temp = temp[::-1]
    if((temp[0] == '{' and temp[1] == '}') or (temp[0] == '[' and temp[1] == ']') or (temp[0] == '(' and temp[1] == ')')):
        print('Balanced')
        return
    print('Unbalanced')
    return


pila = Stack()
pila.push('(')
pila.push(')')
pila.push('[')
pila.push(']')
pila.push('{')
pila.push('}')
pila.printStacks()
valid_parenthesis(pila)
valid_parenthesis(pila)
valid_parenthesis(pila)
