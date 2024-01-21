# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def listLength(head):
    node = ListNode(next=head)
    length = 0
    while node.next:
        length += 1
        node = node.next
    return length

def split(head, n):
    node = ListNode(next=head)
    for i in range(n):
        node = node.next
    head2 = node.next
    node.next = None
    return head2

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = listLength(head)
        d = length // k
        m = length % k

        answer = []
        head1 = head
        for i in range(k):
            n = d
            if i < m:
                n += 1
            head2 = split(head1, n)
            answer.append(head1)
            head1 = head2
        return answer

