class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b>0:
            carry = a&b
            a = a^b
            b = carry<<1
        return a
            

        


if __name__ == '__main__':
    lists=[3,5,7]
    for li in lists:
        print "{0:07b}".format(li)
    so=Solution()
    print so.getSum(-1,100)
