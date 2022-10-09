class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        numset = set(nums)
        return sum(n + diff in numset and n + diff*2 in numset for n in nums[:-2])
