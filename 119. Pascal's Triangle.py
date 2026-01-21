"""
Docstring for 119. Pascal's Triangle
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Set up a base case:
        if numRows == 0:
            return []
        # The first row is also treated as a base case since this is the top of the pyramid
        if numRows == 1:
            return [[1]]
        
        # Memoization allows us to recall the 
        previousRows = self.generate(numRows-1)
        
        # Creating the newest layer here
        newRow = [1] * numRows

        # Populated the values of each row with the math
        for i in range(1, numRows -1):
            newRow[i] = previousRows[-1][i-1] + previousRows[-1][i]
        
        #append the new row
        previousRows.append(newRow)
        return previousRows
