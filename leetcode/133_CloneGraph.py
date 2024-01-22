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
        visited = set()
        clones = dict()
        head = Node(node.val)
        clones[node.val] = head
        queue = deque([[node, head]])
        while queue:
            original, clone = queue.pop()
            if original.val in visited:
                continue
            visited.add(original.val)
            for orinb in original.neighbors:
                if orinb.val in clones:
                    clonb = clones[orinb.val]
                else:
                    clonb = Node(val=orinb.val, neighbors = None)
                    clones[orinb.val] = clonb
                if clone.neighbors is None:
                    clone.neighbors = []
                clone.neighbors.append(clonb)
                queue.appendleft([orinb, clonb])
        return head
