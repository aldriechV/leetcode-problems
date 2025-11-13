"""
74. Search a 2D Matrix
You are given an m x n integer matrix  with the following two properties:

1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.
3. Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity. (I wonder what I'm using :D)

"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        1. Narrow the search to the nearest array 
        2. Binary search once an array is narrowed
        """

        low = 0
        high = len(matrix[0]) - 1
        targetRow = []

        for i in range(len(matrix)):
            if target >= matrix[i][low] and target <= matrix[i][high]:
                targetRow = matrix[i]
                while low <= high:
                    med = (low + high) // 2
                    if targetRow[med] == target:
                        return True
                    elif targetRow[med] > target:
                        high = med - 1
                    else:
                        low = med + 1


        
        return False