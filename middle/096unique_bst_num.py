class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for x in range(n+1)]
        dp[0]=1
        dp[1]=1
        if n<2: return dp[n]
        for x in range(2,n+1):
        	start,end = 1, x
        	total=0
        	for mid in range(start,end+1):
        		total+=dp[mid-start]* dp[end-mid]
        	dp[x] = total
        return dp[n]
so=Solution()
print so.numTrees(3)

