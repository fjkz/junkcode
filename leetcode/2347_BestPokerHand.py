class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if all(suits[0] == suits[i] for i in range(1, len(suits))):
            return "Flush"
        count_rank = {}
        for rank in ranks:
            if not rank in count_rank:
                count_rank[rank] = 1
            else:
                count_rank[rank] += 1
        pair = max(count_rank.values())
        if pair >= 3:
            return "Three of a Kind"
        if pair == 2:
            return "Pair"
        return "High Card"
