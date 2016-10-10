class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for x in range(0,length-1):
        	for y in range(x+1,length):
        		if nums[x]+nums[y]==target:
        			return [x,y]

so = Solution()
print so.twoSum([2, 7, 11, 15],9)