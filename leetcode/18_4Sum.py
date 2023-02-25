class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = set()
        nums.sort()
        for a, na in enumerate(nums[:-3]):
            for b in range(a+1, len(nums)-2):
                nb = nums[b]
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    nc = nums[c]
                    nd = nums[d]
                    s = na + nb + nc + nd
                    if s == target:
                        answer.add((na, nb, nc, nd))
                    if s < target:
                        c += 1
                    else:
                        d -= 1
        return [list(a) for a in answer]
