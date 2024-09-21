class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        i = 1
        answer = [i]
        for j in range(n-1):
            if (i0 := i * 10) <= n:
                i = i0
            elif (i1 := int(str(i + 1).rstrip('0'))) <= n:
                i = i1
            else:
                i = int(str(i // 10 + 1).rstrip('0'))
            answer.append(i)
        return answer
