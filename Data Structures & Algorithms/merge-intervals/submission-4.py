class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        results = [] 

        for currStart, currEnd in intervals:
            # merge when prev interval end time >= curr interval start time 
            if results and results[-1][1] >= currStart:
                results[-1][1] = max(results[-1][1], currEnd)
            else:
                results.append([currStart, currEnd])

        return results