from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = bisect_left(nums, target)
        if a < len(nums) and nums[a] == target:
            return a
        return -1
