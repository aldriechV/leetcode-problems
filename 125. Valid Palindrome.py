"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

- I won't lie the hardest part is filtering the string to only alphanumeric characters and making them all lowercase.
1. Initial Solution:
- Create a new string that contains only the alphanumeric characters from the original string, all converted to lowercase.
- Compare this new string to its reverse to check if it is a palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = "".join([char.lower() for char in s if char.isalnum()])     
    
        return check == check[::-1]