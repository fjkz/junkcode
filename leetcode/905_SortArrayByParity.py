class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        answer = [None] * len(nums)
        i_even = 0
        i_odd = len(nums) - 1
        for n in nums:
            if n % 2 == 0:
                answer[i_even] = n
                i_even += 1
            else:
                answer[i_odd] = n
                i_odd -= 1
        return answer
