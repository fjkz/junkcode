class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) // 2
        return sum(nums[2*i] for i in range(n)) 
