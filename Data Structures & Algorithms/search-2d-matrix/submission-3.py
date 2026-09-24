class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find which row that could be in by looking at first and last index of each row
        row_in = 0

        for row in matrix:
            if row[0] <= target <= row[-1]:
                # perform binary search within that row
                left = 0
                right = len(row) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if row[mid] == target:
                        return True
                    elif (row[mid] <= target): # 
                        left = mid + 1
                    else:
                        right = mid - 1
        return False