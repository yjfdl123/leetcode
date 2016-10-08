class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        import copy
        ret = copy.deepcopy(digits)
        ret.reverse()
        carry = 0
        ret[0]=ret[0]+1
        for idx,num in enumerate(ret):
        	ss = ret[idx] +carry
        	ret[idx] = ss%10
        	carry = ss/10
        if carry==1: ret.append(1)
        ret.reverse()
        return ret
so = Solution()
print so.plusOne([9,9,9,9])
