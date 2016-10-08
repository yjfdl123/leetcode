class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev = [1 for idx in range(rowIndex+1)]
        import copy
        cur = copy.deepcopy(prev)
        

so =Solution()
print so.getRow(4)