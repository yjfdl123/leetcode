#encoding=utf-8
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if nums[0]<nums[-1]:
            return nums[0]
        start, end = 0, len(nums)-1
        while start+1<end:
            mid = (start+end)>>1
            if nums[mid]>nums[start]:
                start=mid
            else:
                end=mid
        return min(nums[start],nums[end])





def main():
	lists = [
		[3,5,7,1,2],
		[1,2,3,4,5],
		[2,1],
		[1],
	]
	so = Solution()
	for li in lists:
		print so.findMin(li)


if __name__ == '__main__':
	main()