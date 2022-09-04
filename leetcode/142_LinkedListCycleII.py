# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        walker = head
        history = {id(walker): walker}
        while walker := walker.next:
            node_id = id(walker)
            if node_id in history:
                return history[node_id]
            history[node_id] = walker
        return None
