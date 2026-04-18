class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2] # swap the child and parent
            i = i // 2

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        
        # New tree with the last node as the root
        res = self.heap[1]
        self.heap[1] = self.heap[len(self.heap)-1]
        self.heap.pop()

        self._percolate_down(1)
        return res


    def top(self) -> int:
        if len(self.heap) <= 1:
            return -1
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        cur = (len(self.heap) - 1) // 2
        
        # check all nodes and percolate down to ensure it's in the correct position
        while cur > 0:
            self._percolate_down(cur)
            cur -= 1
    
    def _percolate_down(self, i):
        while True:
            leftChild, rightChild = i * 2, i * 2 + 1
            smallest = i

            if leftChild < len(self.heap) and self.heap[leftChild] < self.heap[smallest]:
                smallest = leftChild
            if rightChild < len(self.heap) and self.heap[rightChild] < self.heap[smallest]:
                smallest = rightChild
            if smallest == i:
                break
            
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest