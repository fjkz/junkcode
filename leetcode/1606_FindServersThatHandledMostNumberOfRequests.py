from bisect import bisect_left, insort
from heapq import heappush, heappop

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        handle_requests = [0] * k
        available_servers = [srv for srv in range(k)]
        busy_servers = []
        for i, (arrival_time, load_duration) in enumerate(zip(arrival, load)):
            while busy_servers and busy_servers[0][0] <= arrival_time:
                _, srv = heappop(busy_servers)
                insort(available_servers, srv)

            if not available_servers:
                # drop request
                continue

            first_server = i % k
            isrv = bisect_left(available_servers, first_server)
            if isrv < len(available_servers):
                handle_server = available_servers[isrv]
                del available_servers[isrv]
            else:
                handle_server = available_servers[0]
                del available_servers[0]

            handle_requests[handle_server] += 1
            heappush(busy_servers, (arrival_time + load_duration, handle_server))

        answer = []
        max_handle = 0
        for server, handle in enumerate(handle_requests):
            if handle > max_handle:
                max_handle = handle
                answer = [server]
            elif handle == max_handle:
                answer.append(server)
        return answer

