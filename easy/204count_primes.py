import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2: return 0
        ret = [True]* n
        ret[0]=False
        for num in range(2,int(math.sqrt(n))+1):
        	if ret[num-1]:
        		j=num
        		while j*num<=n:
        			ret[j*num-1] = False
        			j+=1
        return ret[:-1].count(True)

so = Solution()
print so.countPrimes(2)
