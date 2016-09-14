#encoding=utf-8
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start<=end:
        	if start==end:
        		return nums[start]
        	mid = (start+end) >> 1
        	if nums[mid]<nums[start]:   #边界处理
        		end = mid 
        	if nums[mid]>nums[end]:
        		start = mid            #边界处理
        	if nums[mid] == nums[start]:
        		start+=1
        		while nums[start]==nums[mid] and start<mid:
        			start+=1
        		return nums[start]
       		return nums[start]




def main():
	lists = [
		[3,5,7,1,2],
		[1,2,3,4,5],
		[1,2,2,2,2,2,1],
		[1,1,1,1,1,1],
		[2,1],
		[1],
	]
	so = Solution()
	for li in lists:
		print so.findMin(li)


if __name__ == '__main__':
	main()