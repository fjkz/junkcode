class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        low = 0
        high = len(nums) - 1
        while low < high:
            if nums[high] == val:
                high -= 1
                continue
            if nums[low] == val:
                nums[low], nums[high] = nums[high], nums[low]
            low += 1
        if nums[low] == val:
            return low
        else:
            return low + 1
