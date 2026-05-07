class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowelAmt = []
        vowels = "aeiouAEIOU"
        for i in s:
            if i in vowels:
                vowelAmt.append(i)
        index = len(vowelAmt)-1
        s = list(s)

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowelAmt[index]
                index -= 1

        return "".join(s)
