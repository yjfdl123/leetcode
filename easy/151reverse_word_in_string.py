class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s=="": return ""
        lst = [word for word in s.split(' ') if word!='']
        lst.reverse()
        ret = ' '.join(lst)
        return ret