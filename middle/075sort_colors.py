#coding=utf-8
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start,mid,end = -1,0,len(nums)
        while mid < end:
        	if mid==start:
        		mid+=1
        	elif nums[mid]==0:
        		start+=1
        		nums[start], nums[mid] = nums[mid],nums[start]
        	elif nums[mid]==2:
        		end-=1
        		nums[end], nums[mid] = nums[mid] ,nums[end]
        	elif nums[mid]==1:
        		mid+=1
        return nums


####这个错误是，并不是所有的情况mid都要加1，交换以后还是要处理的

so = Solution()
print so.sortColors([1,2,0])
print so.sortColors([0])