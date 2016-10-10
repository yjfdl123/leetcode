class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0: return 0
        if x<2: return x
        start,end =1, x/2
        while start<end:
        	mid = (start+end)/2
        	square=mid*mid
        	# print start,end,mid,square
        	if square==x:
        		return mid
        	elif square<x:
        		start=mid+1
        	elif square>x:
        		end=mid-1
        minimum=x
        return start if start*start<=x else start-1
        # sqrt = start
        # for ran in range(start-1,start+2):
        # 	if abs(ran*ran-x)<minimum: 
        # 		minimum = abs(ran*ran-x)
        # 		sqrt=ran
        # return sqrt
so=Solution()
print so.mySqrt(4)
