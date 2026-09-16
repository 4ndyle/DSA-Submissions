"""
3 main conditions: 
currInterval is completely before newInterval
currInterval is completely after newInterval
currInterval is overlapping with newInterval

before: 
if newInterval.end < currInterval.start 

after: 
if newInterval.start > currInterval.end 

overlapping:
if currInterval.start <= newInterval.end and currInterval.end >= newInterval.start: 
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newList = []

        for i in range(len(intervals)):
            currInterval = intervals[i]

            if newInterval[1] < currInterval[0]:
                newList.append(newInterval)
                newList.extend(intervals[i:])
                break
            elif newInterval[0] > currInterval[1]:
                newList.append(currInterval)
            else:
                # update newInterval to represent merged interval 
                newInterval = [min(newInterval[0], currInterval[0]), max(newInterval[1], currInterval[1])]
        else:
            newList.append(newInterval)

        return newList
