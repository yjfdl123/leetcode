class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = -10000000
        asum = 0
        for num in nums:
        	asum += num
        	maxsum = asum if asum > maxsum else maxsum
        	if asum<0:
        		asum = 0
        return maxsum