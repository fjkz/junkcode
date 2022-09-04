# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        tortise = hare = head
        while (tortise := tortise.next) and hare.next and (hare := hare.next.next):
            if tortise is hare:
                return True
        return False
