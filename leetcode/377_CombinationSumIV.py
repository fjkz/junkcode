class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = set(nums)
        combs = [1] + [0] * target
        for n in range(1, target + 1):
            for i in nums:
                if i > n:
                    continue
                combs[n] += combs[n-i]
        return combs[target]
