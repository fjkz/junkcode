class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {n: i for i, n in enumerate(nums)}
        for i1, n1 in enumerate(nums):
            n2 = target - n1
            if n2 in index and index[n2] != i1:
                return [i1, index[n2]]
