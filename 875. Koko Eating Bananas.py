"""
875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
"""


class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        binary search between 0 and max(bananas)
        then the target 
        """
        # Computes the total number of hours needed if Koko eats at speed `value`.
        # For each pile, we need ceil(pile / value) hours.
        def condition(value):
            total = 0
            for pile in piles:
                total += (pile - 1) / value + 1
            return total <= h
                

        #beecause the most amount of bananas we can eat is the highest number of bananas, we also want to account for the fact that we can only get one pile at a time, so anything past the max would not work/
        # we're running a binary search where the values are from 0 to k, here k is the largest pile size
        # we're looking to find a minimum which is why we are returning the left pointer
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
        
