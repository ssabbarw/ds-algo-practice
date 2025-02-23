import math, heapq

class Solution:
    def shortestPath(self, adj, src):
        # code here

        weights = [math.inf] * len(adj)

        pq = []
        weights[src] = 0

        heapq.heappush(pq, (weights[src], src))

        while pq:
            cur_wt, cur, = heapq.heappop(pq)

            for neighbor in adj[cur]:
                if 1 + cur_wt < weights[neighbor]:  # Relaxation step
                    weights[neighbor] = cur_wt + 1
                    heapq.heappush(pq, (weights[neighbor], neighbor))

        return [w if w != math.inf else -1 for w in weights]