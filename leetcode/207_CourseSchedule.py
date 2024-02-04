class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[a].append(b)

        NOT_DONE = 0
        DOING = 1
        DONE = 2

        state = [NOT_DONE for _ in range(numCourses)]
        sorted_list = []

        def visit(n):
            if state[n] is DOING:
                return False
            if state[n] is NOT_DONE:
                state[n] = DOING
                for n2 in g[n]:
                    dag = visit(n2)
                    if not dag:
                        return False
                state[n] = DONE
                sorted_list.append(n)
            return True

        for n in range(numCourses):
            if state[n] is NOT_DONE:
                dag = visit(n)
                if not dag:
                    return False
        #print(sorted_list)
        return True
