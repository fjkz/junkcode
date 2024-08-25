class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        a = self.postorderTraversal(root.left)
        a.extend(self.postorderTraversal(root.right))
        a.append(root.val)
        return a
