class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for list in matrix:
            startNum = list[0]
            endNum = list[len(list) - 1]

            # target is in range of list
            if target >= startNum and target <= endNum:
                # perform binary search on list to find target
                start = 0
                end = len(list)

                while start <= end:
                    middle = (start + end) // 2
                    print(f"middle is {middle}")
                    if target == list[middle]:
                        return True
                    elif target < list[middle]:
                        end = middle - 1
                    else:
                        start = middle + 1

        return False