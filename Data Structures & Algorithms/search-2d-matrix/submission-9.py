class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        T = 0
        B = len(matrix) -1
        vector_with_value = []

        while T <= B:
            mid = (T+B)//2
            if target > matrix[mid][-1]:
                T = mid + 1
            elif target < matrix [mid][0]:
                B = mid -1
            else:
                vector_with_value = matrix[mid][:]
                break
        print (vector_with_value)
        L = 0
        R = len (vector_with_value) -1
        while L <= R:
            mid = (L + R) // 2
            if target > vector_with_value[mid]:
                L = mid + 1
            elif target < vector_with_value [mid]:
                R = mid -1
            else:
                return True
        return False