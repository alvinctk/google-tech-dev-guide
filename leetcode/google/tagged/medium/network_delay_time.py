from heapq import heappop
from heapq import heappush
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        Time Complexity - O(E log E) since heap might store E number of edges and each operation takes log E.
        Space Complexity - O(E) graph and q stores at most E number of entries
        """
        q, seen, adj = [(0, K)], {}, defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        while q:
            time, node = heappop(q)
            if node not in seen:
                seen[node] = time

                for v, w in adj[node]:
                    if v not in seen: heappush(q, (time + w, v))

        return max(seen.values()) if len(seen) == N else -1
