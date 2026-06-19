class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt = [0]
        for i in gain:
            alt.append(i+alt[-1])
        return max(alt)

        