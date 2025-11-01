class Solution:
    def isCycle(self, V, edges):
        # Create adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [0] * V

        # DFS helper function
        def dfs(node, parent):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False

        # Check all components (for disconnected graph)
        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True
        return False
V = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
obj = Solution()
print(obj.isCycle(V, edges))
