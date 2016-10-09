class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ret=[1]
        total = 1
        count = [0]*len(primes)
        cur = [1*prime for prime in primes]
        while total<n:
            mini = min(cur)
            ret.append(mini)
            for index in range(len(cur)):
                if cur[index]==mini:
                    count[index]+=1
                    cur[index] = primes[index]*ret[count[index]]

            total+=1
        # print ret
        return ret[-1]
so = Solution()
print so.nthSuperUglyNumber(10,[2,3,5])
print so.nthSuperUglyNumber(12,[2, 7, 13, 19])