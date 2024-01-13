class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = - 10 ** 9 - 1
        work_sum = 0
        for n in nums:
            work_sum += n
            largest_sum = max(largest_sum, work_sum)
            work_sum = max(0, work_sum)
        return largest_sum
