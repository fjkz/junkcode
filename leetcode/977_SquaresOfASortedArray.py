from collections import deque

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = deque()
        nums = deque(nums)
        while nums:
            if abs(nums[0]) < abs(nums[-1]):
                n = nums.pop()
            else:
                n = nums.popleft()
            answer.appendleft(n*n)
        return list(answer)
