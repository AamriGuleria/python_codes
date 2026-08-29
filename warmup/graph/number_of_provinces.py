class Solution:
    def __init__(self):
        self.groups = []
        self.grouped = set()

    def add_to_group(self, i, j):
        i_group = None
        j_group = None
        for index, group in enumerate(self.groups):
            if i in group:
                i_group = index
            if j in group:
                j_group = index
        if i_group is None and j_group is None:
            self.groups.append({i, j})
        elif i_group is not None and j_group is None:
            self.groups[i_group].add(j)
        elif i_group is None and j_group is not None:
            self.groups[j_group].add(i)
        elif i_group == j_group:
            pass
        else:
            self.groups[i_group].update(self.groups[j_group])
            self.groups.pop(j_group)

        self.grouped.add(i)
        self.grouped.add(j)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    self.add_to_group(i, j)
        for city in range(n):
            if city not in self.grouped:
                self.groups.append({city})
        return len(self.groups)