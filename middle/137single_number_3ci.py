class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=3
        if not nums:
        	return 0
        lsum = []
        for num in nums:
        	index=0
        	while num>0:
        		wei=num&1
        		num = num>>1
        		if len(lsum)>index:
        			lsum[index] = (lsum[index]+wei)%k
        		else:
        			lsum.append(wei)
        		index+=1
        	print index,lsum
        ret = 0
        lsum.reverse()
        for wei in lsum:
        	ret = (ret<<1)|wei
        return ret

so = Solution()
# print so.singleNumber([2,2,3,2])
print so.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])
ret=-1
print -7>>1>>1

