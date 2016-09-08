class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = 0
        maxlen = len(nums)
        while nums[start]!=0 and start<maxlen:
            start+=1
        end = start +1
        while end<maxlen:
            nums[start],nums[end]=nums[end],nums[start]
            while nums[start]!=0:
                start+=1
            end=end+1
            while end<maxlen and nums[end]==0:
                end+=1
	print nums


if __name__=='__main__':
	test = Solution()
	nums=[1]
	test.moveZeroes(nums)
