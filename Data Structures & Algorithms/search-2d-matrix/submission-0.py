class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        L = 0
        R = m*n - 1
        mid = (L+R)//2

        while L<=R:
            mid = (L+R)//2
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] < target:
                L = mid + 1
            else:
                R = mid - 1
        return False