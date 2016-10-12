class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        return (num-1)%9+1
        # if num==0: return 0
        # if num%9==0:
        #     return 9
        # else:
        #     return num%9



    def addDigits2(self, num):
        while num > 9:
            c = 0
            while num:
                c += num % 10
                num /= 10
            num = c
        return num

so=Solution()
print -1%9+1
for x in range(100):
    print x,so.addDigits(x)