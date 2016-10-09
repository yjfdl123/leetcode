class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret=[1]
        count2,count3,count5=0,0,0
        while len(ret)<n:
            mini = min(ret[count2]*2,ret[count3]*3,ret[count5]*5)
            if ret[count2]*2==mini:count2+=1
            if ret[count3]*3==mini:count3+=1
            if ret[count5]*5==mini:count5+=1
            ret.append(mini)
        return ret[-1]



so=Solution()
print so.nthUglyNumber(10)
