from collections import deque

class Solution:
    def isCycle(self, V, edges):
        # Create adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [0] * V

        # BFS helper function
        def bfs(start):
            queue = deque([(start, -1)])  # (node, parent)
            visited[start] = True

            while queue:
                node, parent = queue.popleft()

                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, node))
                    elif neighbor != parent:
                        # Found a visited neighbor that is not parent -> cycle
                        return True
            return False

        # Check all components (for disconnected graph)
        for i in range(V):
            if not visited[i]:
                if bfs(i):
                    return True
        return False


V = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
obj = Solution()
print(obj.isCycle(V, edges))
