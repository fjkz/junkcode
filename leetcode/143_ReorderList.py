class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_list = []
        dummy_head = ListNode(next=head)
        w = dummy_head.next
        while w:
            node_list.append(w)
            next_node = w.next
            w.next = None
            w = next_node
        left = 0
        right = len(node_list) - 1
        while left < right:
            left_node = node_list[left]
            right_node = node_list[right]
            left_node.next = right_node
            if left + 1 < right:
                right_node.next = node_list[left + 1]
            left += 1
            right -= 1
        return dummy_head.next
