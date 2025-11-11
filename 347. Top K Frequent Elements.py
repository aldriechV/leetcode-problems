"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        print(counts)
        final = []
        for i in range(k):
            final.append(sorted(counts, key=counts.get, reverse = True)[i])

        return final