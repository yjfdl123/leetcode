class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = len(s)-1
        lst = list(s)
        while start<end:
            lst[start], lst[end] = lst[end], lst[start]
            start +=1
            end -=1
        return ''.join(lst)

if __name__ == '__main__':
    so=  Solution()
    lists=['abcde','hello.']
    for li in lists:
        print so.reverseString(li)