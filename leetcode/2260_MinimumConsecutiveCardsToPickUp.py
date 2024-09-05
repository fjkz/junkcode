class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        INF = 10**6 + 1
        answer = INF
        nearest =  dict()
        for i, value in enumerate(cards):
            if value in nearest:
                answer = min(answer, i - nearest[value] + 1)
            nearest[value] = i
        if answer == INF:
            return -1
        return answer
