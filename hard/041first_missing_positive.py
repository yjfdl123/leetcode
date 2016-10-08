class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start,end = 0,len(nums)
        count=0
        while start<end :
        	if (nums[start]<=0) or (nums[start]>len(nums)) or (nums[start]==start+1) or (nums[start]==nums[nums[start]-1]):
        		start+=1
        	else:
        		# nums[start], nums[ nums[start]-1 ] = nums[ nums[start]-1 ], nums[start]
        		tmp = nums[start]
        		nums[start] = nums[nums[start]-1]
        		nums[tmp-1]=tmp
        		count+=1
        		# print nums[start], nums[ nums[start]-1 ],nums[ nums[start]-1 ], nums[start]
        		# swap(nums[start], nums[ nums[start]-1 ])
        start=0
        while start<end and nums[start]==start+1:
        	start+=1
        return start+1

so=Solution()
print so.firstMissingPositive([1,2,3,9,10])
print so.firstMissingPositive([1,-2,3,-9,10])
print so.firstMissingPositive([1,2,3])
print so.firstMissingPositive([2,1])
x=[2,1]
x[0],x[1]=x[1],x[0]
print x