import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # print nums
        comp = random.choice(nums)
        # print comp
        num1,num2=[],[]
        for num in nums:
            if num>comp:
                num1.append(num)
            elif num<comp:
                num2.append(num)
        if len(num1)>=k:
            return self.findKthLargest(num1,k)
        elif len(nums)- len(num2)<k:
            return self.findKthLargest(num2,k-(len(nums)-len(num2)))
        else:
            return comp
so=Solution()
print so.findKthLargest([1,7,9,15,3,21,31,100],3)

# x=range(0)
# print random.choice(x)




