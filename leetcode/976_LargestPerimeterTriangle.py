class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        t = [nums.pop() for _ in range(3)]
        while True:
            for i, j, k in [[0, 1, 2], [1, 2, 0], [2, 0, 1]]:
                if t[i] >= t[j] + t[k]:
                    del t[i]
                    break
            else:
                return sum(t)
            if not nums:
                return 0
            t.append(nums.pop())
