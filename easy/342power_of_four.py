class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:return False
        if num==1:return True
        sm2 =num&3
        if sm2!=0:return False
        return True
        
so = Solution()
print so.isPowerOfFour(0)
print so.isPowerOfFour(16)
print so.isPowerOfFour(9)