class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or len(obstacleGrid)==0 or len(obstacleGrid[0])==0:
        	return 0
        hei, wid = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[hei-1][wid-1]==1:
        	return 0
        dp = [ [1 for w in range(wid)] for h in range(hei)]

        for h in range(1,hei):
        	dp[h][0] = 0 if obstacleGrid[h][0]==1 else dp[h-1][0] 
        for w in range(1,wid):
        	dp[0][w] = 0 if obstacleGrid[0][w]==1 else dp[0][w-1]
        for h in range(1,hei):
        	for w in range(1,wid):
        		dp[h][w] = 0 if obstacleGrid[h][w]==1 else dp[h-1][w]+dp[h][w-1]
        return dp[hei-1][wid-1]


a=[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
b=[[]]
c=[[0]]
d=[[1]]
so = Solution()
print so.uniquePathsWithObstacles(a)
print so.uniquePathsWithObstacles(b)
print so.uniquePathsWithObstacles(c)
print so.uniquePathsWithObstacles(d)