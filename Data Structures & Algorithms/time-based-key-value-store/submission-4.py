"""
Plan: 
Use a dict to keep track of the timemap with:
key = key
val = [(value, timestamp)]

Example:
TimeMap timeMap = new TimeMap();
{}

timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
{
    "alice" : [("happy", 1)]
}

timeMap.get("alice", 1);           // return "happy"
Perform a binary search through the list of tuples to find the timeStamp of 1

timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
Perform binary search, if not found, return val on the right pointer 

timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
{
    "alice" : [("happy", 1), ("sad", 3)]
}

timeMap.get("alice", 3);           // return "sad"
"""

from collections import defaultdict

class TimeMap:

    # create a dict to store the keys and values of the TimeMap
    def __init__(self):
        self.timeMap = defaultdict(list)

    # set the input key as the key in the timemap and add (value, timestamp) into list (stored in the val of timeMap)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value,timestamp))
    
    # Perform a binary search in the list from the key to find the timestamp
    def get(self, key: str, timestamp: int) -> str:
        # if the key does not exist in timeMap, return empty string
        if key not in self.timeMap:
            return ""

        # perform a binary search to find the timestamp
        left = 0
        right = len(self.timeMap[key]) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            currTimeStamp = self.timeMap[key][mid][1]

            if currTimeStamp <= timestamp:
                res = self.timeMap[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return res
    




