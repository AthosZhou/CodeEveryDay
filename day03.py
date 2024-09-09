from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dummy = res
        while head.next:
            if head.val != 0:
                dummy.val += head.val
            else:
                dummy.next = ListNode()
                dummy = dummy.next
            head = head.next
        return res.next