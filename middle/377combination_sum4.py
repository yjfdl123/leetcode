class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """        
        nums.sort()
        dp = [0] *(target+1)
        dp[0] = 1
        for tar in range(1,target+1):
        	for num in nums:
        		if tar-num>=0:
        			dp[tar] +=dp[tar-num]
        		else:
        			break
        return dp[target]
so = Solution()
print so.combinationSum4([1,2,3],4)