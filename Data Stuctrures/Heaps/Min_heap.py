import heapq


class MinHeap:
    def __init__(self, minheap):
        heapq.heapify(minheap)
        self.minheap = minheap

    def insert(self, key):
        heapq.heappush(self.minheap, key)

    def getMin(self):
        return self.minheap[0]

    def removeMin(self):
        heapq.heappop(self.minheap)

    def printHeap(self):
        print(self.minheap)
