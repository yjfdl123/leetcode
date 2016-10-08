# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
        	return 0
        leftdep = self.minDepth(root.left)
        righdep = self.minDepth(root.right)
        if leftdep==0 and righdep==0: return 1
        if leftdep==0: return righdep+1
        if righdep==0: return leftdep+1
        return min(leftdep,righdep)+1


print min(1,2)