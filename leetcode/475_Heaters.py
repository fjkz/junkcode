from bisect import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        INF = 10**11
        heaters = [- INF] + sorted(heaters) + [INF]
        furthest_house = 0
        for house in houses:
            near = bisect(heaters, house)
            nearest_heater = min(house - heaters[near - 1], heaters[near] - house)
            furthest_house = max(furthest_house, nearest_heater)
        return furthest_house
