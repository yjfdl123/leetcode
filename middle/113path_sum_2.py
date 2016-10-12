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
        if root==None: return []
        path,ret=[],[]
        self.find(root,sum,path,ret)
        return ret

    def find(self,root,sum,path,ret):
        if root.left==None and root.right==None:
            if root.val==sum:
                path.append(root.val)
                tmp = copy.deepcopy(path)
                ret.append(tmp)
                path.pop()
        else:
            path.append(root.val)
            if root.left!=None: self.find(root.left,sum-root.val,path,ret)
            if root.right!=None: self.find(root.right,sum-root.val,path,ret)
            path.pop()
