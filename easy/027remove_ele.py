class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
        	return 0
        while len(nums)>0:
        	if nums.count(val)>0:
        		nums.remove(val)
        	else:
        		break

        return len(nums)


def main():
	so = Solution()
	li = [3,2,2,3]
	print so.removeElement(li,3)


if __name__ == '__main__':
	main()