# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[Li
        """
        ret=[]
        self.find_path(root,sum,[],ret)
        return ret

    def find_path(self,root,sum,path,ret):
    	if root==None:
    		if 0==sum and ret.count(path)==0 and path:
    			tmp = copy.deepcopy(path)
    			ret.append(tmp)
    	else:
	    	path.append(root.val)
	    	self.find_path(root.left,sum-root.val,path,ret)
	    	self.find_path(root.right,sum-root.val,path,ret)
	    	path.pop()
