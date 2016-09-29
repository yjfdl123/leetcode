class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        dp = [1 for num in nums]
        import sys
        maxl = 1
        for idx,num in enumerate(nums):
        	if idx>0:
        		for j in range(idx):
        			if nums[idx]>nums[j] and dp[idx]<=dp[j] :   dp[idx] = dp[j]+1
        		if dp[idx]>maxl: maxl = dp[idx]
        return maxl






so = Solution()
print so.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print so.lengthOfLIS([1,2,3,4,5,0])
