class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-101, next=head)
        working = dummy
        while working and working.next:
            if working.val == working.next.val:
                working.next = working.next.next
                continue
            working = working.next
        return dummy.next
