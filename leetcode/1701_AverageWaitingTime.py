class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_wait = 0
        busy_until = 0
        for arrival, prepare in customers:
            if arrival >= busy_until:
                finishing = arrival + prepare
            else:
                finishing = busy_until + prepare
            total_wait += finishing - arrival
            busy_until = finishing
        return total_wait / len(customers)
