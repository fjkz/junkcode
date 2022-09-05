from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque([[root, 0]])
        answer = []
        working_level = 0
        level_nodes = []
        while q:
            node, level = q.popleft()
            if level == working_level:
                level_nodes.append(node.val)
            else:
                working_level = level
                answer.append(level_nodes)
                level_nodes = [node.val]
            q.extend([child, level + 1] for child in node.children)
        return answer + [level_nodes]
