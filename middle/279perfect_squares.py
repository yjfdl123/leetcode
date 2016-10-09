class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square=[0]
        num=1
        while num*num<=n:
        	square.append(num*num)
        	num+=1
        ret = [n]*(n+1)
        ret[0] = 0
        for tar in range(1,n+1):
        	mini = n
        	sq=1
        	while sq<num:
        	# for sq in range(num):
        		diff = tar-square[sq]
        		if diff==0:
        			mini=0
        			break
        		elif diff>0:
        			if ret[diff]<mini: mini=ret[diff]
        			sq+=1
        		else:
        			break
        	ret[tar] = mini+1
        return ret[tar]
so = Solution()
# print so.numSquares(7217)
print so.numSquares(9975)
# print so.numSquares(6337)