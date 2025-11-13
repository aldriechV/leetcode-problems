"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets. 
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if i == ")" and top != "(":
                    return False
                if i == "]" and top != "[":
                    return False
                if i == "}" and top != "{":
                    return False
        return len(stack) == 0
