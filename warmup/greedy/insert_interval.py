from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def insert_interval(intervals,newInterval):
            i = 0
            n = len(intervals)
            while i < n and intervals[i][0] < newInterval[0]:
                i += 1
            intervals.insert(i, newInterval)
                
        def merge_intervals(intervals):
            new_list = [intervals[0]]
            for i in range(1, len(intervals)):
                current = intervals[i]
                prev = new_list[-1]
                if prev[1] >= current[0]:
                    prev[1] = max(prev[1], current[1])
                else:
                    new_list.append(current)
            return new_list

        insert_interval(intervals,newInterval)
        return merge_intervals(intervals)
