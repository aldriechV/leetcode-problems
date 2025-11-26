"""
Docstring for 1015. Smallest Integer Divisible by K\

Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.
"""

class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0 or k % 5 == 0: return -1
        
        ones = 1
        while ones % k != 0:
            ones *= 10
            ones += 1
        
        return len(str(ones))
        