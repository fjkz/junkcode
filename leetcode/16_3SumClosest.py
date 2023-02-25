class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = 1000000
        nums.sort()
        for i0, n0 in enumerate(nums):
            i1 = i0 + 1
            i2 = len(nums) - 1
            while i1 < i2:
                n1 = nums[i1]
                n2 = nums[i2]
                s = n0 + n1 + n2
                if abs(target - s) < abs(target - closest):
                    closest = s
                if target - s > 0:
                    i1 += 1
                else:
                    i2 -= 1
        return closest
