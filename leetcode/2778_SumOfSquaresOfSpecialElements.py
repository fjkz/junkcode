class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        specials = [i for i in range(1, n+1) if n % i == 0]
        return sum(nums[i - 1] ** 2 for i in specials)
