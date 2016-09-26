class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for num in nums:
        	if dic.get(num,None):
        		return True
        	else:
        		dic.update({num:True})
        return False


x={"a":1}
print x.get("a",1)
print x.get("b",None)
so = Solution()
x=[1,2,3,4]
print so.containsDuplicate(x)
x.append(4)
print so.containsDuplicate(x)
