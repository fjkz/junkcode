# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        removing_nums = set(nums)
        dummy_head = ListNode(next=head)
        work = dummy_head
        while work.next:
            if work.next.val in removing_nums:
                work.next = work.next.next
                continue
            work = work.next
        return dummy_head.next
