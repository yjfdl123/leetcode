#encoding=utf-8
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0,0
        find = False
        while not find:
        	slow = nums[slow]
        	fast = nums[ nums[fast]]
        	# print slow,fast
        	if slow==fast:
        		find=True
        find = False
        # print 
        slow = 0
        while not find:
        	slow = nums[slow]
        	fast = nums[fast]
        	# print slow,fast
        	if slow==fast:
        		find = True
        return slow

##slow fast是具体指向的数字
so = Solution()
print so.findDuplicate([2,5,9,6,9,3,8,9,7,1])
