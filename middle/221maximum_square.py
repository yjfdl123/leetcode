import copy
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0 or len(matrix[0])==0: return 0
        maximum=0
        hei,wei = len(matrix),len(matrix[0])
        dp=copy.deepcopy(matrix)
        for h in range(hei):
        	for w in range(wei):
        		dp[h][w]=int(matrix[h][w])
        		if dp[h][w]>maximum: maximum=dp[h][w]
        for h in range(1,hei):
        	for w in range(1,wei):
        		if matrix[h][w]=="1":
        			dp[h][w] = min(dp[h-1][w], dp[h][w-1], dp[h-1][w-1]) +1
        			if dp[h][w]>maximum: maximum=dp[h][w]
        return maximum*maximum
