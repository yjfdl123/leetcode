#coding=utf-8
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n<=0:return []
        if n==1: return [[1]]
        matrix = [[0 for y in range(n)] for x in range(n)]
        self.loop(matrix,0,n-1,0,n-1,1,n*n)
        return matrix

    def loop(self,matrix, hstart,hend,wstart,wend,count,n2):
        if hstart<=hend and wstart<=wend:
            #第一行
            tmp=wstart
            while tmp<=wend:
                matrix[hstart][tmp]=count
                tmp+=1
                count+=1
            # ret.extend( matrix[hstart][wstart:wend+1] )
            if hend>hstart:
                #最后一列
                for h in range(hstart+1,hend+1):
                    # print h,wend
                    matrix[h][wend]=count
                    count+=1
                    # ret.append(matrix[h][wend])
                if wend>wstart:
                    #最后一行
                    for w in range(wend-1,wstart-1,-1):
                        matrix[hend][w]=count
                        count+=1
                        # ret.append(matrix[hend][w])
                    #第一列
                    for h in range(hend-1,hstart,-1):
                        matrix[h][wstart]=count
                        count+=1
                        # ret.append( matrix[h][wstart])
            self.loop(matrix,hstart+1,hend-1,wstart+1,wend-1,count,n2)
            # ret.extend( self.loop(matrix,hstart+1,hend-1,wstart+1,wend-1))
            # return ret        
so=Solution()
print so.generateMatrix(10)


