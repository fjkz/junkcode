class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        root = slow.next
        slow.next = None
        left_tree = self.sortedListToBST(head)
        right_tree = self.sortedListToBST(root.next)
        return TreeNode(root.val, left_tree, right_tree)
