from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        q = deque([root])
        while q:
            node = q.popleft()
            for child in [node.left, node.right]:
                if child:
                    q.append(child)
            val1 = node.val
            val2 = k - val1
            if val1 == val2:
                continue
            # find val2 element
            node = root
            while node:
                if node.val == val2:
                    # found
                    return True
                if node.val > val2:
                    node = node.left
                    continue
                if node.val < val2:
                    node = node.right
                    continue
        return False
