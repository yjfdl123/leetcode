class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu=[]
        ac = 0
        for num in nums:
            ac+=num
            self.accu.append(ac)
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0: 
            return self.accu[j]
        else:
            return self.accu[j]-self.accu[i-1]