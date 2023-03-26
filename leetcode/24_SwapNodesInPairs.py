class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        work = dummy
        while work.next and work.next.next:
            n1 = work.next
            n2 = work.next.next
            n1.next, n2.next, work.next = n2.next, n1, n2
            work = n1
        return dummy.next
