class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sumset = sum(set(nums))
        repetition = sum(nums) - sumset
        N = len(nums)
        loss = N * (N + 1) // 2 - sumset
        return [repetition, loss]
