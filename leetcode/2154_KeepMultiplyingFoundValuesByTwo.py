class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numset = set(nums)
        work = original
        while work in numset:
            work *= 2
        return work
