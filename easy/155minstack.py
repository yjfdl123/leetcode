class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mindata = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        if not self.mindata:
            self.mindata.append(x)
        else:
            top = self.mindata[-1]
            self.mindata.append(x) if x<top else self.mindata.append(top)
   
    def pop(self):
        """
        :rtype: void
        """
        if self.data:
            self.mindata.pop(-1)
            return self.data.pop(-1)
        else:
            return None
        

    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]
        else:
            return None

        

    def getMin(self):
        """
        :rtype: int
        """
        if self.mindata:
            return self.mindata[-1]
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()