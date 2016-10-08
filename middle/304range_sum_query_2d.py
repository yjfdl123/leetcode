class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.ma =[[]]
        if len(matrix)>0 and len(matrix[0])>0:
            self.ma= [[0 for n in range(len(matrix[0]))] for m in range(len(matrix)) ]
            self.ma[0][0]=matrix[0][0]
            for n in range(1,len(matrix[0])):
                self.ma[0][n]=self.ma[0][n-1]+matrix[0][n]
            for m in range(1,len(matrix)):
                self.ma[m][0]=self.ma[m-1][0]+matrix[m][0]
            for m in range(1,len(matrix)):
                for n in range(1,len(matrix[0])):
                    self.ma[m][n]= self.ma[m-1][n]+ self.ma[m][n-1]-self.ma[m-1][n-1]+matrix[m][n]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1==0 and col1==0: return self.ma[row2][col2]
        if row1==0: return self.ma[row2][col2]- self.ma[row2][col1-1]
        if col1==0: return self.ma[row2][col2]- self.ma[row1-1][col2]
        return self.ma[row2][col2] - self.ma[row1-1][col2] - self.ma[row2][col1-1] + self.ma[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
numMatrix = NumMatrix(matrix)
print numMatrix.sumRegion(0, 1, 2, 3)
print numMatrix.sumRegion(1, 2, 3, 4)