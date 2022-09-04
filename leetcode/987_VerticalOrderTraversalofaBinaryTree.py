from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        answer = {}
        q = deque([[root, 0, 0]])
        while q:
            node, row, col = q.popleft()
            if not col in answer:
                answer[col] = [node.val]
            else:
                answer[col].append(node.val)

            if node.left:
                q.append([node.left, row + 1, col - 1])
            if node.right:
                q.append([node.right, row + 1, col + 1])

        s = sorted([[key, sorted(val)] for key, val in answer.items()])
        return [v for k, v in s]
