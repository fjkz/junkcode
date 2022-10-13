class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        h = len(numbers) - 1
        while l < h:
            twosum = numbers[l] + numbers[h]
            if twosum == target:
                return [l+1, h+1]
            if twosum < target:
                l += 1
            else:
                h -= 1
