class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        b = 0
        a = 0
        l = 0
        o = 0 
        n = 0

        for i in text:
            if i == 'b': b+=1
            elif i == "a": a += 1
            elif i == "l": l += 1
            elif i == "o": o += 1
            elif i == "n": n +=1
        
        return min(b, a, l//2, o//2, n)