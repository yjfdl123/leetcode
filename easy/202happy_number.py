class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: return False
        if n==1: return True
        using=[]
        while using.count(n)==0:
        	using.append(n)
        	x=n
        	lst=[]
        	while x>0:
        		lst.append(x%10)
        		x=x/10
        	n=sum([a*a for a in lst])
        return n==1
so=Solution()
print so.isHappy(11)
