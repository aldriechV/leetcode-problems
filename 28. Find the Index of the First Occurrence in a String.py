"""
Docstring for 28. Find the Index of the First Occurrence in a String


Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Initial Solution:
1. Loop through the haystack string up to the point where the remaining substring is at least as long as needle.
2. For each position, check if the substring of haystack starting at that position and having the same length as needle matches needle.
3. Return -1 otherwise 
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
                

