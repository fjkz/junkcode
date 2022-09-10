class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        bins = [n % 2 for n in nums]
        odd_idx = [i for i, n in enumerate(bins) if n]
        edges = [(i, i + k - 1) for i in range(0, len(odd_idx) - k + 1)]
        answer = 0
        for le, re in edges:
            if le == 0:
                left_mergen = odd_idx[le]
            else:
                left_mergen = odd_idx[le] - odd_idx[le-1] - 1
            if re == len(odd_idx) - 1:
                right_mergen = len(bins) - odd_idx[re] - 1
            else:
                right_mergen = odd_idx[re + 1] - odd_idx[re] - 1
            answer += (left_mergen + 1) * (right_mergen + 1)
        return answer
