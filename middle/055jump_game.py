class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        boolst = [False for num in nums]
        boolst[0] = True
        start,end = 0,len(nums)
        far = 0
        while start<end :
            if start<=far:
                if start+nums[start]>far : far=start+nums[start]
                if far>=end-1:return True
                start+=1
            else:
                return False
        return far>=end-1







so = Solution()
print so.canJump([2,3,1,1,4])
print so.canJump([3,2,1,0,4])





        # boolst = [False for num in nums]
        # boolst[0] = True
        # for idx in range(len(nums)):
        #   if boolst[idx]:
        #       for step in range(1,nums[idx]+1):
        #           if idx+step<len(nums) and not boolst[idx+step]:
        #               boolst[idx+step] = True
        # return boolst[len(nums)-1]