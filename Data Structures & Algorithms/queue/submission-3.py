class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left = self.right = None

    def isEmpty(self) -> bool:
        if self.right:
            return False
        else:
            return True

    def append(self, value: int) -> None:
        newNode = ListNode(value)
        # queue is not empty
        if self.right:
            self.right.next = newNode
            newNode.prev = self.right
            self.right = newNode
        else: # empty queue
            newNode.prev = self.right
            self.right = newNode
            self.left = newNode

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value)
        if self.left:
            newNode.next = self.left
            self.left.prev = newNode
            self.left = newNode
        else: # queue is empty
            self.left = newNode
            self.right = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            poppedVal = self.right.val
            self.right = self.right.prev
            if self.right:
                self.right.next = None
            else: # there was only one element 
                self.left = None
                self.right = None
            return poppedVal


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        poppedVal = self.left.val
        self.left = self.left.next
        if self.left:
            self.left.prev = None
        else:
            self.left = None
            self.right = None
        return poppedVal