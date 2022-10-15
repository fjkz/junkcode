# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fast = dummy
        slow = dummy
        precede = 0
        while fast:
            fast = fast.next
            if precede > n:
                slow = slow.next
            precede += 1
        if slow.next:
            slow.next = slow.next.next
        return dummy.next
