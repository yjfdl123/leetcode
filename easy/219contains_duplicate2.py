class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for idx,num in enumerate(nums):
        	print idx,num,dic
        	if dic.get(num,None)!=None:
        		if idx - dic[num] <=k:
        			return True
        		else:
        			dic[num] = idx
        	else:
        		dic.update({num:idx})
        return False

so = Solution()
print so.containsNearbyDuplicate([-1,-1],1)

if 0:
	print 123