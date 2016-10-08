class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        for num in nums2:
        	if nums1.count(num)>0:
        		ret.append(num)
        		nums1.remove(num)
        return ret
so = Solution()
print so.intersect([1,2,2,1],[2,2])
