#coding=utf-8
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start,end=0,len(nums)-1
        while start<=end:
        	mid=(start+end)>>1
        	if nums[mid]==target:
        		return True
        	if nums[mid]<nums[start]:   #mid右边是有序数组
        		if target>nums[mid] and target<=nums[end]:
        			start=mid+1
        		else:
        			end=mid-1
        	elif nums[mid]>nums[start]:  #mid左边是有序数组
        		if target>=nums[start] and target<nums[mid]:
        			end=mid-1
        		else:
        			start=mid+1
        	else:
        		start+=1
        return False

so=Solution()
print so.search([1,2,4,5],3)
print so.search([3,1],1)
print so.search([3,5,1],1)
print so.search([3,1,2,2,2],1)