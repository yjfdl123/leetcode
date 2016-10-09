class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<=1: return nums
        vote1,vote2 = None,None
        count1,count2 = 0,0
        start,end = 0,len(nums)
        while start<end:
        	if nums[start]==vote1:
        		count1+=1
        	elif nums[start]==vote2:
        		count2+=1
        	elif count1==0:
        		vote1 = nums[start]
        		count1= 1
        	elif count2==0:
        		vote2 = nums[start]
        		count2= 1
        	else:
        		count1-=1
        		count2-=1
        	start+=1
        ret = []
        len3 = len(nums)/3
        if nums.count(vote1)>len3 : ret.append(vote1)
        if vote2!=vote1 and nums.count(vote2)>len3 : ret.append(vote2)
        return ret

so = Solution()
# print so.majorityElement([1,2,3,1,2])
# print so.majorityElement([2,2])
print so.majorityElement([1,1,1,3,3,2,2,2])