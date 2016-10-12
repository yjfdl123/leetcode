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
        small,big=1,n
        while small<=big:
        	mid=(small+big)>>1
        	ret=guess(mid)
        	if ret==0:
        		return mid
        	elif ret==1:
        		small=mid+1
        	else:
        		big=mid-1
        return 0