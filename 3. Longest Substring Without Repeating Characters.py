"""
Docstring for 3. Longest Substring Without Repeating Characters
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = []
        maxLen = 0
        n = len(s)
        for i in range(n):
            j = i
            while j < n and s[j] not in sub:
                sub.append(s[j])
                j += 1
            maxLen = max(maxLen, j - i)
            sub = []
        return maxLen
    
    