# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
        	return 0
        ret = 0
        if root.left!=None:
        	if root.left.left==None and root.left.right==None:
        		ret+= root.left.val
        	else:
        		ret+= self.sumOfLeftLeaves(root.left)
        ret+=self.sumOfLeftLeaves(root.right)
       	return ret

