"""
        1
    2       3
  4   5    6
Pre: 1 -> 2 -> 4 -> 5 -> 3 -> 6
Post: 4 -> 5 -> 2 -> 6 -> 3 -> 1
Inorders: 1 -> 2 -> 3 -> 4 -> 5 -> 6
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if (data < self.data):  # Insertar en la izquierda
                if (self.left is None):
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif (data > self.data):  # Insertar en la derecha
                if (self.right is None):
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:  # Declarar Raiz
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    # InOrder
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    # Preorder traversal
    # Root -> Left ->Right
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res

    # Postorder traversal
    # Left ->Right -> Root
    def postOrerTraversal(self, root):
        res = []
        if root:
            res = self.postOrerTraversal(root.left)
            res = res + self.postOrerTraversal(root.right)
            res.append(root.data)
        return res


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)+1)


def isBalanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)

    if((abs(lh - rh) <= 1) and isBalanced(root.left) is True and isBalanced(root.right) is True):
        return True

    return False


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print('In-Order:', root.inorderTraversal(root))
print('Pre-Order:', root.preorderTraversal(root))
print('Post-Order:', root.postOrerTraversal(root))
print('El arbol esta balanceado:', isBalanced(root))
