class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        turn = 0
        answer = 0
        while turn < k:
            largest = happiness.pop()
            if largest < turn:
                break
            answer += largest - turn
            turn += 1
        return answer
