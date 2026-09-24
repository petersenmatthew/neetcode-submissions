class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # binary search the ACTUAL row
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                ## THIS IS THE ROW
                # perform binary search within that row
                row = matrix[mid]
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
            
            elif matrix[mid][0] >= target:
                right = mid - 1
                ## ITS ROW BEFORE
            else:
                left = mid + 1
                ## ITS ROW AFTER
        return False