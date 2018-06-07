class Heap():
    capacity = 10
    size = 0

    items = []

    def getLeftChildIndex(parentIndex):
        return 2 * parentIndex + 1
    def getRightChildIndex(parentIndex):
        return 2 * parentIndex + 2
    def getParentIndex(childIndex):
        return (childIndex - 1) / 2

    def hasLeftChild(index):
        return getLeftChildIndex(index) < size
    def hasRightChild(index):
        return getRightChildIndex(index) < size
    def hasParent(index):
        return getParentIndex(index) >= 0

    def leftChild(index):
        return items[getLeftChildIndex(index)]
    def rightChild(index):
        return items[getRightChildIndex(index)]
    def parent(index):
        return items[getParentIndex(index)]
