# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)

        l1, l2 = list1, list2
        cur = res
        while l1 and l2:
            l1_val = l1.val
            l2_val = l2.val
            if l1_val <= l2_val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            while l1:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
        elif l2:
            while l2:
                cur.next = l2
                l2 = l2.next
                cur = cur.next

        return res.next