from collections import deque

def bfs(node):
    visited = {node}
    queue = deque([node])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.value)
        for neighbor in node.neighbor:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


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
print(bfs(a))


