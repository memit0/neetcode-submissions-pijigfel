# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find length
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1

        # Handle edge case with dummy node
        dummy = ListNode(0)
        dummy.next = head

        count = 0
        cur, prev = head, dummy
        while cur:
            if count == length - n:
                nextNode = cur.next
                prev.next = nextNode

            prev = cur 
            cur = cur.next
            count += 1

        return dummy.next

        # [1, 2, 3, 4] n = 2, count = 0
        # prev=1, cur=2, count=1
        # prev=2, cur=3, count=2
        # count == n: nextNode = 4, prev= 2