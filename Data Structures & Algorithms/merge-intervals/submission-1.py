class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals in ascneding order by start time
        intervals.sort(key = lambda x : x[0])

        # create list to store results
        results = []
        resultsIndex = 0

        # merge intervals 
        for i in range(len(intervals)):
            currInterval = intervals[i]

            if not results:
                results.append(currInterval)
            else:
                prevInterval = results[resultsIndex]

                if prevInterval[1] >= currInterval[0]:
                    results[resultsIndex] = [prevInterval[0], max(prevInterval[1], currInterval[1])]
                else:
                    newInterval = [currInterval[0], currInterval[1]]
                    results.append(newInterval)
                    resultsIndex += 1

        return results