# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ret=[]
        self.find(root,k,ret)
        return ret[-1]

    def find(self,root,k,ret):
        if root!=None:
            self.find(root.left,k,ret)
            if len(ret)<k:
                ret.append(root.val)
                self.find(root.right,k,ret)





