
from typing import List
from collections import defaultdict, Counter


# class Solution:
#     def treeDiameter(self, edges: List[List[int]]) -> int:
#         """
#         O(TN). T is the number of terminals, N is the number of nodes.
#         TLE (22/26 passed.)
#         """
#         neighbors = defaultdict(set)
#         for edge in edges:
#             neighbors[edge[0]].add(edge[1])
#             neighbors[edge[1]].add(edge[0])

#         terminals = []
#         for node, node_n in neighbors.items():
#             if len(node_n) == 1:
#                 terminals.append(node)
#         max_diameter = 0
#         for terminal in terminals:
#             # for each terminal, use BFS to calculate the depths of the tree rooted as the terminal
#             queue = []
#             visited = set()
#             queue.append(terminal)
#             visited.add(terminal)
#             depths = {}
#             depths[terminal] = 0
#             while queue:
#                 node = queue.pop(0)
#                 for node_n in neighbors[node]:
#                     if node_n not in visited:
#                         queue.append(node_n)
#                         visited.add(node_n)
#                         depths[node_n] = depths[node] + 1
#             max_length = max(depths.values())
#             if max_length > max_diameter:
#                 max_diameter = max_length
#         return max_diameter

# class Solution:
#     def treeDiameter(self, edges: List[List[int]]) -> int:
#         """
#         Complexity: O(T^2 * P). T is the numnber of terminals. P is the max path length
#         """
#         graph = defaultdict(set)
#         for a, b in edges:
#             graph[a].add(b)
#             graph[b].add(a)
#         bfs = {(u, None) for u, nex in graph.items() if len(nex) == 1}
#         move = 0
#         while bfs:
#             new_bfs = set()
#             for u, pre in bfs:
#                 for v in graph[u]:
#                     if v != pre:
#                         counter[(v, u)] += 1
#                         new_bfs.add((v, u))
#             bfs = new_bfs
#             move += 1
#         return max(move - 1, 0)

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
        DFS solution. Time complexity: O(N)
        """
        self.diameter = 0

        def dfs(node, pre):
            d1 = d2 = 0
            for nex in graph[node]:
                if nex != pre:
                    d = dfs(nex, node)
                    if d > d1:
                        d1, d2 = d, d1
                    elif d > d2:
                        d2 = d
            if d1 + d2 > self.diameter:
                self.diameter = d1 + d2
            return d1 + 1
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        dfs(0, None)
        return self.diameter


if __name__ == '__main__':
    solution = Solution()
    edges = [[0, 1], [0, 2]]
    print(solution.treeDiameter(edges))
    edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
    print(solution.treeDiameter(edges))
