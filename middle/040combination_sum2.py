#coding=utf-8
import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates.sort()
        left = copy.deepcopy(candidates)
        self.backtracking(candidates,0,left,target,[],ret)
        return ret

    def backtracking(self,candidates,start,left,target,solu,ret):
    	if target==0:    		
    		# find = False
    		# for value in ret:
    		# 	if value==solu:
    		# 		find=True
    		if ret.count(solu)==0:
    			tmp = copy.deepcopy(solu)
    			ret.append(tmp)
    	else:
	    	for index in range(start,len(candidates)):
	    		num = candidates[index]
	    		if left.count(num)>0 and target-num>=0:
	    			solu.append(num)
	    			left.remove(num)
	    			self.backtracking(candidates,index+1,left,target-num,solu,ret)
	    			left.append(num)
	    			solu.pop()
	    		else:                  #####没有这个减枝，竟然就超时了
	    			break




so = Solution()
print so.combinationSum2([10, 1, 2, 7, 6, 1, 5],8)