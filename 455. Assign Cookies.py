class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        cookies = 0
        kids = 0

        while cookies < len(s) and kids < len(g):
            if s[cookies] >= g[kids]:
                cookies += 1
                kids += 1
            else:
                cookies += 1
        return kids