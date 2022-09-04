class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(subs):
            if len(subs) == 0:
                return [[]]
            answer = []
            for word in wordDict:
                if subs.startswith(word):
                    ans = backtrack(subs[len(word):])
                    for a in ans:
                        answer.append([word] + a)
            return answer
        aa = backtrack(s)
        return [" ".join(a) for a in aa]
