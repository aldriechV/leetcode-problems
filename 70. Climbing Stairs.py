"""
Docstring for 70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 1
        y = 1
        total = 0
        if n == 1:
            return 1
        for i in range(n-1):
            total = x + y
            y = x
            x = total
        return total

