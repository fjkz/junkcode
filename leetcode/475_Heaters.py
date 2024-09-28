from bisect import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        furthest_house = 0
        for house in houses:
            near = bisect(heaters, house)
            if near == 0:
                nearest_heater = heaters[0] - house
            elif near == len(heaters):
                nearest_heater = house - heaters[-1]
            else:
                nearest_heater = min(house - heaters[near - 1], heaters[near] - house)
            furthest_house = max(furthest_house, nearest_heater)
        return furthest_house
