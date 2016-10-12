#coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        self.depth={}

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            self.depth[root]=0
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.right):    ##先判断子节点都是平衡的
            leftdp  = self.depth[root.left]
            rightdp = self.depth[root.right]
            if abs(leftdp- rightdp)>1: 
                return False
            else:
                self.depth[root]=max(leftdp, rightdp)+1
                return True
        else:
            return False


x={}
x[0]=1
x[None]=3
print x