# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            l1 = lists.pop(0) 
            l2 = lists.pop(0) if lists else None
            lists.append(self.merge(l1, l2))

        return lists[0]

    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy

        l1_pointer, l2_pointer = l1, l2
        while l1_pointer and l2_pointer:
            if l1_pointer.val <= l2_pointer.val:
                cur.next = l1_pointer
                l1_pointer = l1_pointer.next
            else:
                cur.next = l2_pointer
                l2_pointer = l2_pointer.next
            cur = cur.next

        while l1_pointer:
            cur.next = ListNode(l1_pointer.val)
            l1_pointer = l1_pointer.next
            cur = cur.next
        
        while l2_pointer:
            cur.next = ListNode(l2_pointer.val)
            l2_pointer = l2_pointer.next
            cur = cur.next

        return dummy.next


