class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, COLS * ROWS - 1
        
        while l <= r:
            m = l + ((r - l) // 2)
            rows = m // COLS
            cols = m % COLS
            m = l + ((r - l) // 2)

            if matrix[rows][cols] > target:
                r = m - 1
            elif matrix[rows][cols] < target:
                l = m + 1
            else:
                return True
        return False
