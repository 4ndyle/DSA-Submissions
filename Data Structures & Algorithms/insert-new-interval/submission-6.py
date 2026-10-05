"""
Plan:
results = [] 

for i in range(len(intervals)):
    # determine which interval to add
    if intervals[i].start < newInterval.start:
        currInterval = intervals[i]
    otherwise, 
        currInterval = newInterval

    if currInterval.start >= newInterval.start:
        results.append(newInterval)
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert interval into list 
        results = [] 
        inserted = False 

        for currStart, currEnd in intervals:
            if not inserted and currStart >= newInterval[0]:
                results.append(newInterval)
                inserted = True

            results.append([currStart, currEnd])

        if not inserted: results.append(newInterval)

        # merge intervals 
        prevEndTime = -1 
        merged = []

        for currStart, currEnd in results:
            # merge when start is less than prev end time 
            if merged and currStart <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], currEnd)
            else:
                merged.append([currStart, currEnd])

        return merged 