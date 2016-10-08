class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:return False
        if n==1:return True
        carry=0
        while n!=0:
        	carry+= n&1
        	n=n>>1
        	if carry>1:return False
        return True


        
so = Solution()
print so.isPowerOfTwo(0)
print so.isPowerOfTwo(6)
print so.isPowerOfTwo(9)