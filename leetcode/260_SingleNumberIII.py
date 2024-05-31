class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        onceNums = set()
        for n in nums:
            if n in onceNums:
                onceNums.remove(n)
                continue
            onceNums.add(n)
        assert len(onceNums) == 2
        return list(onceNums)
