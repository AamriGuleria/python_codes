from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count=0
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        prev_end = intervals[0][1]
        for i in range(1,n):
            if intervals[i][0] < prev_end:
                count+=1
            else:
                prev_end = intervals[i][1]
        return count
