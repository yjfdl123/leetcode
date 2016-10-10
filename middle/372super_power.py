class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        x=0
        for num in b:
        	x=x*10+num
        return self.loop(a,x)%1337
    def loop(self,a,x):
    	if x==1: return a
    	# if x==0: return 1
    	if x%2==0:
    		return self.loop(a*a,x/2)
    	else:
    		return self.loop(a*a,x/2)*a
so=Solution()
print so.superPow(2147483647,[2,0,0])