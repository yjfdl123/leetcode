class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        more, count = 0,0
        for num in nums:
        	if count==0 :
        		more=num
        		count+=1
        	elif count>0:
        		if more==num :
        			count+=1
        		else:
        			count-=1
        return more




x={"a":1}
del x["a"]
print x
so = Solution()
print so.majorityElement([1,1,2,2,2,3])