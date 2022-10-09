from bisect import bisect_left

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        N = len(nums)
        answer = 0
        found = {}
        for i0, n0 in enumerate(nums[:-2]):
            n1 = n0 + diff

            if n1 in found:
                i1 = found[n1]
            else:
                i1 = bisect_left(nums, n1, lo=i0+1)
                if i1 >= N or nums[i1] != n1:
                    continue

            n2 = n1 + diff
            i2 = bisect_left(nums, n2, lo=i1+1)
            if i2 >= N or nums[i2] != n2:
                continue

            answer += 1
            found[n2] = i2
        return answer
