class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        total = 0
        for i in costs:
            if coins < i:
                return total
            else:
                coins -= i
                total += 1
        return total