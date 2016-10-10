class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {num:1 for num in nums}
        maximum=0
        start=0
        length = len(nums)
        while start< length:
        	if dic.get(nums[start],None)==1:
        		count=0
        		small=nums[start]
        		while dic.get(small,None)==1:
        			count+=1
        			del dic[small]
        			small-=1
        		big = nums[start]+1
        		while dic.get(big,None)==1:
        			count+=1
        			del dic[big]
        			big+=1
        		if count>maximum: maximum=count
        	start+=1
        return maximum
so=Solution()
print so.longestConsecutive([100, 4, 200 , 2])
