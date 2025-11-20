"""717. 1-bit and 2-bit Characters


We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
"""

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) -1 :
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == len(bits) -1