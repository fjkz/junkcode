class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        if all(n == 1 for n in nums):
            return len(nums) - 1

        answer = 0

        # states
        SPLITTED = 0
        SPLITTING = 1
        COUNTING = 2

        # initial state
        state = SPLITTED
        count1 = 0
        count2 = 0

        for n in nums + [0]:
            if state == SPLITTED:
                if n == 1:
                    state = COUNTING
                    count2 += 1
                    continue
                continue
            elif state == SPLITTING:
                if n == 1:
                    state = COUNTING
                    count2 = 1
                    continue
                state = SPLITTED
                count1 = 0
                count2 = 0
                continue
            else:
                if n == 1:
                    count2 += 1
                    continue
                answer = max(count1 + count2, answer)
                state = SPLITTING
                count1 = count2
                count2 = 0

        return answer

