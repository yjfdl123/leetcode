class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
        	return None
        self.left_pro = [1]        
        pro = 1
        for idx in range(1,len(nums)):
        	pro = pro * nums[idx-1]
        	self.left_pro.append(pro)
        pro = 1
        self.right_pro = [1]
        for idx in range(len(nums)-1,0,-1):
        	pro = pro * nums[idx]
        	self.right_pro.append(pro)
        self.right_pro.reverse()
        ret = map(lambda x,y:x*y,self.left_pro,self.right_pro)
        return ret


so=Solution()
print so.productExceptSelf([1,2,3,4,5,0])
print so.productExceptSelf([1,2])
x=[1,2,3]
print x.reverse()
print x
print range(3,1,-1)