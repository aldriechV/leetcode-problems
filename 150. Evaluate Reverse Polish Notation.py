"""
Docstring for 150. Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        res = 0
        for i in tokens:
            if i == "/":
                varOne = int(stack.pop())
                varTwo = int(stack.pop())
                res = float(varTwo) / varOne
                stack.append(int(res))
            elif i == "+":
                varOne = stack.pop()
                varTwo = stack.pop()
                res = varTwo + varOne
                stack.append(res)
            elif i == "-":
                varOne = stack.pop()
                varTwo = stack.pop()
                res = varTwo - varOne
                stack.append(res)
            elif i == "*":
                varOne = stack.pop()
                varTwo = stack.pop()
                res = varTwo * varOne
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[-1]