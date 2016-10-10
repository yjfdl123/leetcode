class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n<=0:return []
        if n==1: return [1]
        return self.loop(0,n,0,n,1,n*n)

    def loop(self,hstart,hend,wstart,wend,count,n2):
    	ret = []
    	if hend<hstart or wend<wstart: return ret
    	#第一行
    	tmp=wstart
    	while tmp<=wend:
    		
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

