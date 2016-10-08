class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        boolst = [False for num in nums]
        boolst[0] = True
        for idx in range(len(nums)):
        	if boolst[idx]:
        		for step in range(1,nums[idx]+1):
        			if idx+step<len(nums) and not boolst[idx+step]:
        				boolst[idx+step] = True
        return boolst[len(nums)-1]


so = Solution()
print so.canJump([2,3,1,1,4])
print so.canJump([3,2,1,0,4])