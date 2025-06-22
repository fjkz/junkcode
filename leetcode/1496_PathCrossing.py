class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        visited = set([(x, y)])
        move = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }
        for label in path:
            dx, dy = move[label]
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
