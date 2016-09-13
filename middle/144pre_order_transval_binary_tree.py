# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tran = []
        if root:
        	tran.append(root.val)
        	tran.extend( self.preorderTraversal( root.left) )
        	tran.extend( self.preorderTraversal( root.right) )
        return tran


x=[]
x.extend([1,2,3])
x.extend([])
print x
