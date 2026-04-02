class TimeMap:

    """
    input: 
    """

    def __init__(self):
        # create a hashmap to represent the timemap, with
        # key: name
        # val: list of times 
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # create list for timemap name if not exist 
        if key not in self.timemap:
            self.timemap[key] = []

        # add timestamp to name (key)
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # use a binary search to find the right most value of the timestamp, if it does not exist, the binary search will record the last 
        # value before the search is terminated 
        result = ""
        timeStampsList = self.timemap.get(key, [])

        left, right = 0, len(timeStampsList) - 1

        while left <= right:
            mid = (left + right) // 2
            currentValue = timeStampsList[mid][0]
            currentTimeStamp = timeStampsList[mid][1]

            if currentTimeStamp <= timestamp:
                # search right and set result to the current timestamp value (in case it does not exist, we will get the time < timestamp)
                result = currentValue
                left = mid + 1
            else:
                # search left
                right = mid - 1

        return result