class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1: return 0
        ugly=[1,2,3]
        while len(ugly)<n:
            mini= min([self.find_next_ugly(ugly,2), self.find_next_ugly(ugly,3), self.find_next_ugly(ugly,5)])
            ugly.append( mini )
        return ugly[-1]

    def find_next_ugly(self,ugly,base):
        start,end = 0,len(ugly)-1
        while start<=end:
            mid = (start+end)/2
            if (ugly[mid]*base>ugly[-1]) and (ugly[mid-1]*base<ugly[-1]):
                return ugly[mid]*base
            elif ugly[mid]*base<ugly[-1]:
                start=mid+1
            else: 
                end=mid-1
so=Solution()
print so.nthUglyNumber(372)
