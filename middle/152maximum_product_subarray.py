class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        amin, amax = [1], [1]
        import sys
        maxret = -sys.maxint -1
        for idx,num in enumerate(nums):
        	lst = [num, amin[-1]*num, amax[-1]*num]
        	amin.append( min(lst))
        	amax.append( max(lst))
        	if amax[-1]>maxret : maxret=amax[-1]
        return maxret

## 这个错误的地方在于是返回更新值，而不是数组之
        

so = Solution()
print so.maxProduct([3,2,-4,6])
print so.maxProduct([3,2,-4,-3,6])
print so.maxProduct([-3,0,-4,2,0])