class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for i in moves:
            if i == "U":
                y += 1
            elif i == "D":
                y -= 1
            elif i == "L":
                x -= 1
            else:
                x += 1
        
        return True if x == 0 and y == 0 else False

# Faster solution
class fasterSolution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return True if moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R") else False
