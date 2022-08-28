from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        level_value = {}
        queue = deque()
        queue.append((1, root))
        while queue:
            level, node = queue.popleft()
            if not level in level_value:
                level_value[level] = node.val
            else:
                level_value[level] += node.val
            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))
        max_val, negative_level = max((v, - k) for k, v in level_value.items())
        return - negative_level
