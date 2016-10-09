class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev=[1]
        row=1
        while row<=rowIndex:
        	nex=[0]*(len(prev)+1)
        	nex[0],nex[-1]=prev[0],prev[-1]
        	for index in range(1,len(nex)-1):
        		nex[index]=prev[index-1]+prev[index]
        	prev,nex=nex,[]
        	row+=1
        return prev


        

so =Solution()
print so.getRow(3)