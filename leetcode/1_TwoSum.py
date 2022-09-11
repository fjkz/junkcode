from bisect import bisect_left

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {n: 0 for n in nums}
        for n in nums:
            count[n] += 1
        for n1 in nums:
            n2 = target - n1
            if n1 == n2 and count[n1] >= 2:
                i1 = nums.index(n1)
                i2 = nums.index(n2, i1 + 1)
                return [i1, i2]
            if n1 != n2 and n2 in count:
                return [nums.index(n1), nums.index(n2)]
