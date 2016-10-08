class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        hei = len(matrix)
        if hei==0: return False
        wid = len(matrix[0])
        if wid==0: return False
        posy=0
        posx=wid-1
        while  posx>=0 and posy<hei:
        	if matrix[posy][posx] == target: return True
        	if target<matrix[posy][posx] :
        		posx-=1 
        	else:
        		posy+=1
        return False
x=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
so =Solution()
print so.searchMatrix(x,5)
print so.searchMatrix(x,20)
