class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        tlist1 = {word: i for i, word in enumerate(list1)}
        tlist2 = {word: i for i, word in enumerate(list2)}
        common = set(list1) & set(list2)
        answer = []
        max_xsum = 9**9
        for word in common:
            xsum = tlist1[word] + tlist2[word]
            if xsum < max_xsum:
                answer = [word]
                max_xsum = xsum
            elif xsum == max_xsum:
                answer.append(word)
        return answer
