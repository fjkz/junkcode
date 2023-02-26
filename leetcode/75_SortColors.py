class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # bubble sort
        N = len(nums)
        for i in range(N - 1):
            for j in range(N - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

