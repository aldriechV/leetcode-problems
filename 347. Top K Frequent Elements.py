"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Solution
1. Create a hash map to count occurrences of each element.
2. Sort the hash map by values in descending order.
3. Create a for loop that iterates through the first k elements of the sorted hash map and appends the keys to the final answer list.

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