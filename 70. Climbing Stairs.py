"""
Docstring for 70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

1. Initial Solution:
- Based on the pattern of the number of ways to reach each step, we can see that the number of ways to reach step n is the sum of the ways to reach steps n-1 and n-2.
- Create a recurisive function that calculates the number of ways to reach the nth step by summing the ways to reach the (n-1)th and (n-2)th steps.
- Make the base cases for when n is 1 or 2.
- Runtime Complexity: O(2^n) due to the exponential growth of recursive calls. This causes TLE!
- Space Complexity: O(n) due to the call stack.

2. Optimized Solution:
- Use an iterative approach to calculate the number of ways to reach each step up to n.
- Initialize two variables to store the number of ways to reach the last two steps.
    - You could also create a list of memoization to store the number of ways to reach each step.
- Iterate from step 3 to n, updating the two variables at each step. 
- Runtime Complexity: O(n) since we only loop through the steps once.
- Space Complexity: O(1) since we only use a constant amount of space.
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

