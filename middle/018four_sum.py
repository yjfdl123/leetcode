class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length<4: return 0
        nums.sort()
        for sp in range(length-3):
        	newtar = target-nums[sp]
        	start=sp+1
        	mid=start+1
        	end = length
