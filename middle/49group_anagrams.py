class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        totaldic = {}
        for word in strs:
        	find = False
        	for base,item in totaldic.iteritems():
        		same = True
        		if len(word)!=len(base):
        			same=False
        		else:
	        		for char,fre in item["frequency"].iteritems():
	        			if word.count(char)!=fre:
	        				same=False
	        				break
        		if same:
        			item["words"].append(word)
        			find = True
        	if not find:
        		totaldic.update({word:{"words":[word]}})
        		fredic={}
        		for ch in word:
        			if fredic.get(ch,None):
        				fredic[ch]+=1
        			else:
        				fredic.update({ch:1})
        		totaldic[word].update({"frequency":fredic})
        ret =[]
        for word,item in totaldic.iteritems():
        	ret.append(item["words"])
        return ret



        			


so = Solution()
x=["", "", "tan", "ate", "nat", "bat"]
print so.groupAnagrams(x)