class MinHeap:
    def __init__(self):
        self.size = 0
        self.items = []

    def get_items(self):
        return self.items

    def get_size(self):
        return self.size

    def getLeftChildIndex(parentIndex):
        return 2 * parentIndex + 1

    def getRightChildIndex(parentIndex):
        return 2 * parentIndex + 2

    def getParentIndex(self, childIndex):
        return (childIndex - 1) / 2

    def hasLeftChild(self, index):
        return getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return getRightChildIndex(index) < self.size

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def leftChild(self, index):
        return self.items[getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.items[getRightChildIndex(index)]

    def parent(self, index):
        return self.items[self.getParentIndex(index)]

    def swap(self, index1, index2):
        item1 = self.items[index1]
        self.items[index1] = self.items[index2]
        self.items[index2] = item1

    def peek(self):
        if self.size == 0:
            return None
        return items[0]

    def poll(self):
        if size == 0:
            return None
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return item

    def add(self, item):
        self.size += 1
        self.items.append(item)
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.parent(index) > self.items[index]:
            self.swap(index, self.getParentIndex(index))
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while (hasLeftChild(index)):
            smallerChildIndex = getLeftChildIndex(index)
            if hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = getRightChildIndex(index)
            if self.items[index] < self.items[smallerChildIndex]:
                break
            else:
                self.swap(smallerChildIndex, index)
            index = smallerChildIndex

H = MinHeap()
H.add(5)
H.add(7)
H.add(3)
H.add(11)
print(H.items)

    
