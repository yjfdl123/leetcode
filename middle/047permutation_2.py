class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ori = nums
        import copy
        nex = copy.deepcopy(nums)
        ret = [ori]
        find = True
        while find:
        	self.nextPermutation(nex)
        	if nex==ori:
        		find = False
        	else:
        		ret.append(copy.deepcopy(nex))
        return ret


    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)>1:
        	v_rev =len(nums)-2
        	while v_rev>=0 and nums[v_rev]>=nums[v_rev+1]:
        		v_rev= v_rev-1
        	start = 0
        	if v_rev>=0:
        		swapidx = v_rev+1
        		import sys
        		maxnum = sys.maxint
        		for i in range(v_rev+1,len(nums)):
        			if nums[i]<maxnum and nums[i]>nums[v_rev]:
        				swapidx = i
        				maxnum = nums[i]
        		nums[v_rev],nums[swapidx] = nums[swapidx],nums[v_rev]
        		start = v_rev+1
        	tmp = nums[start:]
        	tmp.sort()
        	nums[start:] = tmp


so = Solution()
print so.permuteUnique([1,2,3])