"""

392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        - Two pointers: One on S and one on T
        - increment through pointer T if you the letters don't match
        - if they do, increment through both pointers
        """
        sPointer = 0
        tPointer = 0
        sLen = len(s)
        tLen = len(t)
        while sPointer < sLen and tPointer < tLen:
            if s[sPointer] == t[tPointer]:
                sPointer += 1
                tPointer += 1
            else:
                tPointer += 1
        if sPointer == sLen:
            return True
        return False