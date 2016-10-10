class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<0: return False
        if num<2: return True
        start,end =1, num/2
        while start<end:
        	mid = (start+end)/2
        	square=mid*mid
        	if square==num:
        		return True
        	elif square<num:
        		start=mid+1
        	elif square>num:
        		end=mid-1
        return start*start==num
so=Solution()
print so.isPerfectSquare(10)
