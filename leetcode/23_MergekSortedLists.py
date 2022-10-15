from heapq import heappush, heappop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        nodes = []
        for lst in lists:
            node = ListNode(next=lst)
            while node := node.next:
                nodes.append(node)
                heappush(heap, (node.val, len(nodes) - 1))
        answer = ListNode()
        node = answer
        while heap:
            nodeidx = heappop(heap)[1]
            node.next = nodes[nodeidx]
            node = node.next
        return answer.next
