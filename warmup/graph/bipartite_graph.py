from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        A = set()
        B = set()
        n = len(graph)
        for node in range(n):
            if node in B:
                for j in graph[node]:
                    if j in B:
                        return False
                    A.add(j)
            else:
                A.add(node)
                for j in graph[node]:
                    if j in A:
                        return False
                    B.add(j)

        return True