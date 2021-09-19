"""
Max heap -
            15
        13          11
    7       5    8    10
3      1
Min heap - 
        1 -> min
    3       5
7      8  9   1O

Heapq = Min Concept
"""


class Heaps:
    def __init__(self):
        self.heap = []

    def getParentPosition(self, i):
        return int((i-2)/2)

    def getLeftChildPosition(self, i):
        return 2*i+1

    def getRightChildPosition(self, i):
        return 2*i+2

    def hasParent(self, i):
        return self.getParentPosition(i) < len(self.heap)

    def hasLeftChild(self, i):
        return self.getLeftChildPosition(i) < len(self.heap)

    def hasRightChild(self, i):
        return self.getRightChildPosition(i) < len(self.heap)

    def insert(self, key):
        self.heap.append(key)
        self.heapify(len(self.heap)-1)

    def getMax(self):
        return self.heap[0]

    def heapify(self, i):
        while(self.hasParent(i) and self.heap[i] > self.heap[self.getParentPosition(i)]):
            self.heap[i], self.heap[self.getParentPosition(
                i)] = self.heap[self.getParentPosition(i)], self.heap[i]
            i = self.getParentPosition(i)

    def printHeap(self):
        print(self.heap)

    def mostElement(self, k):
        dict = {}
        count = 0
        results = []
        for key in range(len(self.heap)):
            x = self.heap[key] in dict
            dict[self.heap[key]] = count
            if(x):
                num = x+1
                dict[self.heap[key]] = num
        for t, v in dict.items():
            if(v == k):
                results.append(t)
        print(results)
        return results


heap = Heaps()
arr = ["i", "am", "coder", "i", "love", "coding", "love"]
k = 2

for i in arr:
    heap.insert(i)

heap.printHeap()
heap.mostElement(k)
