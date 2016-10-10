class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        k=k%length
        k=length-k
        if k>0:
        	nums.extend(nums[:k])
        	for idx in range(k,len(nums)):
        		nums[idx-k]=nums[idx]
        	for idx in range(k):
        		nums.pop()
        return nums
so=Solution()
print so.rotate([1,2,3,4,5],4)


        	