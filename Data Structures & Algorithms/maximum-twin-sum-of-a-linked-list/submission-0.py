# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # The twin of a node i is n-1-i
        # Return the max twin sum

        # [4, 2, 2, 3]
        # 4,2 3,2
        # node 0 is the twin of node 3 -> 4 + 3 = 7
        # node 1 is the twin of node 2 -> 2 + 2 = 4

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHead = slow

        # Reverse the second half
        cur = secondHead
        prev = None
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        
        cur = prev
        res = 0 
        while cur:
            res = max(res, head.val + cur.val)
            head = head.next
            cur = cur.next
        
        return res