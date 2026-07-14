class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        1. The only combinations exist on a string of numbers 1-9
        2. Why not just slide window, check range
        3. If the placement adds a 0, (i.e 999 to 1000) just extend the window and try again?
        """
        allWeNeed = "123456789"
        l = str(low)
        # bound for maybe how long we can make a str high
        h = str(high)
        ans = []
        # We can use i to decide length of the string? But we add it with the lowest length since i will never iterate past h's lenghth
        for i in range(len(l), len(h)+1):
            # J is used to create our sliding window, we use it as the lowest, the highest can be added with the length of i will stay consistent since we are doing a loop in a loop
            # we use 10 - i since realistically no number is going above 10, it also lets us stop at 9 on our string to let us extend the window by incrementing i
            for j in range(10 - i):
                currNum = int(allWeNeed[j:j+i])
                if low <= currNum <= high:
                    ans.append(currNum)
        return ans

