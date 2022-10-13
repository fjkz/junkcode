from copy import copy

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        copyk = copy(nums[-k:])
        for i, n in enumerate(nums[:-k]):
            nums[i + k] = n
        for i, n in enumerate(copyk):
            nums[i] = n
