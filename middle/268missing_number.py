class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        tsum = (length*(length+1))/2
        for num in nums:
        	tsum-=num
        return tsum



if __name__ == '__main__':
	so = Solution()
	lists=[ [0,1,3],[0,2]]
	for li in lists:
		print so.missingNumber(li)
