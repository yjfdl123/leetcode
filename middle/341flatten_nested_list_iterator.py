# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue=[]
        # if nestedList.isInteger():
        #     self.queue.append(nestedList.getInteger())
        # else:
        #     self.init(nestedList.getList())
        self.init(nestedList)
        self.index=0

    def init(self,nestlist):
        for nest in nestlist:
            if nest.isInteger():
                self.queue.append(nest.getInteger())
            else:                
                self.init(nest.getList())
    def next(self):
        """
        :rtype: int
        """
        if self.index<len(self.queue):
            val=self.queue[self.index]
            self.index+=1
            return val
        else:
            return 0
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index<len(self.queue)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())