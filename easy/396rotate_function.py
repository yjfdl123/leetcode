class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
        	return 0
        import sys
        maxp = -sys.maxint-1
        num = len(A)
        for x in range(len(A)):
        	xishu = range(num-x,num )  + range(0,num-x)
        	pro = sum( map(lambda x,y:x*y,xishu,A ) )
        	maxp = pro if pro>maxp else maxp
        return maxp
        	


if __name__ == '__main__':
	a = [4,3,2,6]
	so = Solution()
	print so.maxRotateFunction(a)
import sys
print -sys.maxint-1
print range(3,3)
print range(2,3)
