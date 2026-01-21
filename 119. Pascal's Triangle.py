"""
Docstring for 119. Pascal's Triangle
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 1. Set up a base case:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        previousRows = self.generate(numRows-1)
        #creating the last layer here
        newRow = [1] * numRows

        for i in range(1, numRows -1):
            newRow[i] = previousRows[-1][i-1] + previousRows[-1][i]
        
        previousRows.append(newRow)
        return previousRows
    