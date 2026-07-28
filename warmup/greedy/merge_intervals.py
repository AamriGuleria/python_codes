from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        new_list = [intervals[0]]
        n = len(intervals)
        for i in range(1,n):
            current = intervals[i]
            prev = new_list[-1]
            if current[0]<=prev[1]:
                prev[1]=max(current[1],prev[1])
            else:
                new_list.append(current)
        return new_list