"""

739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.


"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []

         # loop from right to left
        for i in range(n - 1, -1, -1):
            # 1) pop while current temp is >= temp at stack top
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                 stack.pop()

            # 2) if stack not empty, the top is the next warmer day
            if stack:
                answer[i] = stack[-1] - i

            # 3) push current index
            stack.append(i)

        return answer