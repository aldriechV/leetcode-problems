class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        total = 0
        L = 0
        R = 0
        B = 0 
        for i in moves:
            if i == "L":
                L += 1
            elif i == "R":
                R += 1
            else:
                B += 1

        return abs(L - R) + B
