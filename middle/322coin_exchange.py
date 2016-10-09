def consutime(func):
    def wrapper(*args,**kwargs):
        import time
        start = time.time()
        ret = func(*args,**kwargs)
        print "consume:",time.time()-start
        return ret
    return wrapper
class Solution(object):
    @consutime
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        import sys
        dic = { idx:sys.maxint for idx in range(amount+1)}
        dic[0]=0
        for tsum in range(1,amount+1):
            mins = sys.maxint
            for coin in coins:
                if tsum - coin >=0 and dic[tsum-coin]<mins:
                    mins = dic[tsum-coin]
            dic[tsum] = min(dic[tsum], mins+1)
        return dic[amount] if dic[amount]!=sys.maxint else -1

so=Solution()
print so.coinChange([1,2,5],11)
print so.coinChange([2],3)
print so.coinChange([70,177,394,428,427,437,176,145,83,370],7582)