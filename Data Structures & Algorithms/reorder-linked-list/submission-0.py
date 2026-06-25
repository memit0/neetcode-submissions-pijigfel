class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Identify the midpoint
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHead = slow.next
        slow.next = None

        # Split and reverse second half
        cur = secondHead
        prev = None
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        
        # Merge the two linked lists
        cur1, cur2 = head, prev
        while cur2:
            tmp1, tmp2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = tmp1
            cur1, cur2 = tmp1, tmp2