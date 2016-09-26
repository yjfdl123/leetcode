class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        maxsum = sum(nums)
        if maxsum<s:
        	return 0
        minlen = len(nums)
        start, end = 0, 1
        tsum = 0
        while end<=len(nums):
        	tsum = sum(nums[start:end])
        	minlen = min(minlen,end-start) if tsum>=s else minlen
        	if tsum>s:
        		start+=1
        	else:
        		end+=1
        return minlen
        	


so = Solution()
print so.minSubArrayLen(7,[2,3,1,2,4,3])