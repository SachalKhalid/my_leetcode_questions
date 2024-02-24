class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        adj = [[] for _ in range(n)]
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        q = deque([(0, (src, 0))])
        dist = [float('inf')] * n
        dist[src] = 0

        while q:
            stops, (node, cost) = q.popleft()

            if stops > K:
                continue

            for adjNode, edW in adj[node]:
                if cost + edW < dist[adjNode] and stops <= K:
                    dist[adjNode] = cost + edW
                    q.append((stops + 1, (adjNode, cost + edW)))

        if dist[dst] == float('inf'):
            return -1
        return dist[dst]
