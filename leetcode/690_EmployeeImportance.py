"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {e.id: e for e in employees}

        def dfs(i):
            n = employee_dict[i]
            return n.importance + sum(dfs(s) for s in n.subordinates)

        return dfs(id)
