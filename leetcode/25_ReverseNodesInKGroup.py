def hasNextKNodes(node, k):
    work = node
    for i in range(k):
        if work.next:
            work = work.next
            continue
        return False
    return True

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        khead = dummy
        while khead and hasNextKNodes(khead, k):
            n1 = khead.next
            n2 = n1.next
            for i in range(k-1):
                t = n2.next
                n2.next = khead.next
                n1.next = t
                khead.next = n2
                n2 = t
            khead = n1
        return dummy.next
