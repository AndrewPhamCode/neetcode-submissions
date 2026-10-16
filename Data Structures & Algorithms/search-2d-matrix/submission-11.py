class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + ((r - l) // 2)
            rows, cols = m // COLS, m % COLS 
            val = matrix[rows][cols]

            if val > target:
                r = m - 1
            elif val < target:
                l = m + 1
            else:
                return True
        return False


