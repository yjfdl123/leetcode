class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        for num in nums:
        	x^=num
        return x
        

if __name__ == '__main__':
	lists = [ [1,3,5,5,3],[3],[2222,2222]]
	so = Solution()
	for ls in lists:
		print so.singleNumber(ls)

print '{0:010b}'.format(12)
print '{0:010b}'.format(11)
print 12^11