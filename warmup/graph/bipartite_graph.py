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

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        A = set()
        B = set()
        n = len(graph)
        for node in range(n):
            if node in A or node in B:
                continue
            A.add(node)
            stack = [node]

            while stack:
                node = stack.pop()
                if node in B:
                    for j in graph[node]:
                        if j in B:
                            return False
                        if j not in A:
                            A.add(j)
                            stack.append(j)

                else:
                    for j in graph[node]:
                        if j in A:
                            return False
                        if j not in B:
                            B.add(j)
                            stack.append(j)
        return True