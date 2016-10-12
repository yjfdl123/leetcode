import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: return False
        x=math.log(n,3)
        print x
        intx = int(round(x))
        print intx
        return abs(x-intx)<0.0000000000001

so=Solution()
print so.isPowerOfThree(129140162)
print so.isPowerOfThree(59049)
# print help(math)
# print math.log(27,3)
# print round(2.5231321)