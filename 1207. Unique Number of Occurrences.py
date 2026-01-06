"""
Docstring for 1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

NEED COMMENTS
"""






class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occ = {}
        for i in arr:
            if i in occ:
                occ[i] += 1
            else:
                occ[i] = 1
        
        return len(set(occ.values())) == len(occ.values())

        