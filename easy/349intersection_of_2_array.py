class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))


so = Solution()
print so.intersection([1,2,2,1],[2,2])
x=set([1,2,3])
y=set([2,3])
# print help(y)
# print x.intersection(y)