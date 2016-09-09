class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        maxproduct = [1,1,1]
        for i in range(2,n+1):
                maxproduct.append(0)
                maxproduct[i] = max ( [ max(j*(i-j), j*maxproduct[i-j], maxproduct[j]*(i-j), maxproduct[j]*maxproduct[i-j]) for j in range(1,i)] ) 
        return maxproduct[n]

if __name__ == '__main__':
        so = Solution()
        lists=[2,1,3,4,5,6,10,30,0,50]
        for li in lists:
                print so.integerBreak(li)


'''
这道题目写的真是漂亮