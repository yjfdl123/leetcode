class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
        	return 0
        height, width = len(grid), len(grid[0])
        mat = []
        for h in range(height):
        	newline = []
        	for w in range(width):
        		if h==0:
        			x = grid[h][w] if w==0 else newline[w-1]+grid[h][w]
        			newline.append(x)
        		else:
        			newline.append(mat[h-1][0]) if w==0 else newline.append( min(mat[h-1][w], newline[w-1] ) )
        			newline[-1] += grid[h][w]
        	print h,' ',newline
        	mat.append(newline)
        return mat[height-1][width-1]


so = Solution()
print so.minPathSum([[1,2],[1,1]])
print so.minPathSum([[1,2],[1,2]])




