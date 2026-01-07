"""
Docstring for 155. Min Stack



Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 """


class MinStack(object):

 
    # Standard initialization for a stack, but I am using a min stack in order to keep track of the smallest value
    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # add to the lowest stack normally, but for the minimum stack we add a tracker to see if the value appended is currently smaller than the smallest number on the min stack. 
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
        else:
            min_track = self.min[-1]
            if val < min_track:
                self.min.append(val)
            else:
                self.min.append(min_track)

    # pop is done to both stacks in order to account for if the smallest value was removed from the normal stack. 
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min.pop()

    # returns the top value of the normal stack
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    #return the topmost value of the min stack
    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
