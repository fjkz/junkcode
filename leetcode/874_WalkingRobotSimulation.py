class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(tuple(obs) for obs in obstacles)
        position = (0, 0)
        direction = (0, 1)
        answer = 0
        for cmd in commands:
            if cmd == -2:
                direction = (- direction[1], direction[0])
                continue
            if cmd == -1:
                direction = (direction[1], - direction[0])
                continue
            k = cmd
            for step in range(k):
                next_position = (position[0] + direction[0], position[1] + direction[1])
                if next_position in obstacle_set:
                    break
                position = next_position
            answer = max(answer, position[0] ** 2 + position[1] ** 2)
        return answer
