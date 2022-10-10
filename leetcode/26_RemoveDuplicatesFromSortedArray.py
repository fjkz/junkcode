class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        last = None
        for np in nums:
            nums[k] = np
            if np != last:
                k += 1
            last = np
        return k
