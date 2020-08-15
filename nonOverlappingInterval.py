# Source: https://leetcode.com/problems/non-overlapping-intervals/
# Type: Greedy

import sys

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda interval: interval[1])
        lastInterval = -sys.maxsize
        count = 0
        for interval in intervals:
            if interval[0] >= lastInterval:
                count += 1 
                lastInterval = interval[1]
        return len(intervals) - count
