class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {s: 0 for s in set(arr)}
        for s in arr:
            count[s] += 1
        duplicated = set(s for s, c in count.items() if c >= 2)
        distincts = [s for s in arr if s not in duplicated]
        if k > len(distincts):
            return ""
        return distincts[k-1]
