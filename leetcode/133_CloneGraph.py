"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        head = Node(node.val, [])
        clones = {node.val: head}
        queue = deque([[node, head]])
        while queue:
            original, clone = queue.pop()
            for orinb in original.neighbors:
                if orinb.val in clones:
                    clonb = clones[orinb.val]
                else:
                    clonb = Node(orinb.val, [])
                    clones[orinb.val] = clonb
                    queue.appendleft([orinb, clonb])
                clone.neighbors.append(clonb)
        return head
