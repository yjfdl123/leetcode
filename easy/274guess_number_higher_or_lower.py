# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1: return 0
        if n==1:return 1
        start,end=1,n
        while start<end+1:
        	mid = (start+end)>>2
        	ret = guess(mid)
        	if ret==0:
        		return mid
        	elif ret<0:
        		start=mid+1
        	else:
        		end = mid-1
