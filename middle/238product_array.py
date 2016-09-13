class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
        	return 0
        if len(nums)==1:
        	return nums[0]
        leftpro = [nums[0]]
        for index in range(1,len(nums)):
        	leftpro[index] = leftpro




x=range(1,10)
print x
so = Solution()
print so.productExceptSelf(x)