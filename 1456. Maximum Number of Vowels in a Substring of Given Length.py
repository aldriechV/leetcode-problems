class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = "aeiou"
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1
        
        maxCount = count

        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            
            maxCount = max(count, maxCount)
        return maxCount
        
