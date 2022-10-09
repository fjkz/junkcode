from bisect import bisect_left

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        for i0, n0 in enumerate(nums[:-2]):
            if n0 > 0:
                break
            for i1, n1 in enumerate(nums[i0+1:-1]):
                i1 += i0 + 1
                n2 = - n0 - n1
                i2 = bisect_left(nums, n2, lo=i1+1)
                if i2 >= len(nums) or nums[i2] != n2:
                    continue
                answer.add((n0, n1, n2))
        return [[n0, n1, n2] for n0, n1, n2 in answer]
