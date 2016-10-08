#coding=utf-8
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0 or len(matrix[0])==0:
        	return []
        return self.loop(matrix,0,len(matrix)-1,0,len(matrix[0])-1)

    def loop(self,matrix,hstart,hend,wstart,wend):
    	ret = []
    	if hend<hstart or wend<wstart: return ret
    	#第一行
    	ret.extend( matrix[hstart][wstart:wend+1] )
    	if hend>hstart:
    		#最后一列
    		for h in range(hstart+1,hend+1):
    			print h,wend
    			ret.append(matrix[h][wend])
    		if wend>wstart:
    			#最后一行
    			for w in range(wend-1,wstart-1,-1):
    				ret.append(matrix[hend][w])
    			#第一列
    			for h in range(hend-1,hstart,-1):
    				ret.append( matrix[h][wstart])
    	ret.extend( self.loop(matrix,hstart+1,hend-1,wstart+1,wend-1))
    	return ret






        
x=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
y=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
so = Solution()
# print so.spiralOrder(x)
print so.spiralOrder(y)