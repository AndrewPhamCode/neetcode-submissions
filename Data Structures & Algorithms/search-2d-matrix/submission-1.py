class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for rows in range(len(matrix)):
            for columns in range(len(matrix[0])):
                if matrix [rows][columns] == target:
                    return True
        return False
        