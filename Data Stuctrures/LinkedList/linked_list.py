# 1 -> 2 -> 5 -> 6 -> 7
"""
pointer, next, val
O(n)
O(1) - Add
O(1) - Del
"""


class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            # __import__("ipdb").set_trace()
            current.next = newNode
        else:
            self.head = newNode

    def delete(self, data):
        current = self.head
        # Aplica si es el primero
        if(current is not None):
            if(current.data == data):
                self.head = current.next
                current = None
                return
        # Busqueda despues del primero y antes del ultimo
        while(current):
            if(current.data == data):
                break
            prev = current
            current = current.next
        # Aplica si es el ultimo
        if(current == None):
            return
        prev.next = current.next
        current = current.next
        # print(prev.data, current.data)
        prev = None

    def search(self, data):
        current = self.head
        pos = 0
        while(current):
            if(current.data == data):
                print('Dato encontrado esta en la posicion', pos)
            pos = pos+1
            current = current.next

    def printAllNodes(self):
        current = self.head
        while(current):
            print(current.data, sep=" ")
            current = current.next

    # Detectar si hay ciclos anidados -> Circulo
    def detectCycle(self):
        if(self.head == None):
            return
        fast = slow = self.head
        while(slow and fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # Detectamos si coninciden al dar la vuelta gracias a l nodo Fast
                print(fast.data, slow.data)
                self.removeLoop(slow)
                return

    # Eliminar el ciclo anidado
    def removeLoop(self, loop_node):
        pointer1 = self.head
        while(True):
            pointer2 = loop_node
            while(pointer2.next != loop_node and pointer2.next != pointer1):
                pointer2 = pointer2.next
            if(pointer2.next == pointer1):
                break
            pointer1 = pointer1.next
        pointer2.next = None
        return

    # Recorrer el arreglo en reversa
    def reverseList(self):
        prev = None  # Nodo previo
        current = self.head
        while(current):
            next = current.next  # Nodo siguiente
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return


""" list = LinkedList()
list.insert(10)
list.insert(20)
list.insert(30)
list.insert(40)
list.insert(50)
list.printAllNodes()
print("Empezamos a hacer el recorrido inverso")
list.reverseList()
list.printAllNodes() """

"""
# Empezamos a crear un ciclo de linkedList - Esto se genera en el Indice 4
list.head.next.next.next.next.next = list.head.next.next
# print(list.head.next.next.next.next.next.data, list.head.next.next.data)
list.detectCycle()
print("La lista despues de detectar el ciclo")
list.printAllNodes()
"""
