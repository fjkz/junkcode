class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        answer = 0
        pp = 0
        pt = 0
        while pp < len(players) and pt < len(trainers):
            if players[pp] <= trainers[pt]:
                answer += 1
                pp += 1
                pt += 1
                continue
            pp += 1
        return answer
