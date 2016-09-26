class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        if len(nums)==1:
        	return nums[0]
        start, end = 0, len(nums)
        while start < end:
        	mid = (start + end) >> 1
        	if mid == 0 :
        		if nums[mid] > nums[mid+1]:
        			return nums[mid]
        		else:
        			start = mid + 1
        	if mid == len(nums)-1 and nums[mid] > nums[mid-1]:
        		return nums[mid]
        	if nums[mid]>nums[mid-1] and nums[mid] > nums[mid+1]
