# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # Find kth node
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            groupNext = kth.next

            # Cut the group off
            groupStart = groupPrev.next
            kth.next = None

            # Reverse the isolated group
            newHead = self.reverse(groupStart)

            # Reconnect
            groupPrev.next = newHead
            groupStart.next = groupNext

            # Move to the next group
            groupPrev = groupStart

    
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev