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