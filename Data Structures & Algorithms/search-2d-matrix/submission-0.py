class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log(m*n))
        # intuition: binary search the position of the first element
        # check the row, then check the column
        n = len(matrix) - 1     # row length
        m = len(matrix[0]) - 1  # column length

        l = 0
        r = n

        res_row = 0

        # checks which row its in
        while l <= r:
            mid = (l+r) // 2
            if matrix[mid][m] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                res_row = mid
                break

        # checks the column position 
        l = 0
        r = m

        while l <= r:
            mid = (l+r) // 2
            if matrix[res_row][mid] < target:
                l = mid + 1
            elif matrix[res_row][mid] > target:
                r = mid - 1
            else:
                return True

        return False


        