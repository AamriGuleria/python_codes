# Go as deep as possible before backtracking.
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in node.neighbor:
        dfs(neighbor, visited)


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbor = []

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.neighbor = [b, c]
b.neighbor = [a]
c.neighbor = [a]
nodes = [a, b, c, d]

visited = set()
for node in nodes:
    if node not in visited:
        dfs(node, visited)
dfs(a, visited)
print(visited)