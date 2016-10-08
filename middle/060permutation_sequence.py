class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [1]
        for x in range(1,n+1):
            fac.append( fac[-1]*x)
        print fac
        end = n
        ret = []
        unuse = range(n+1)
        while end>0:
            if k%fac[end-1]==0:
                nindex = k/fac[end-1]
                ret.append(unuse[nindex])
                unuse.remove(ret[-1])
                ret.extend(unuse[1:])
                break
            nindex = (k/fac[end-1])+1
            k = k%fac[end-1]
            ret.append(unuse[nindex])
            unuse.remove(ret[-1])
            end-=1
        ret = [str(x) for x in ret]
        return ''.join(ret)



so = Solution()
print so.getPermutation(3,6)