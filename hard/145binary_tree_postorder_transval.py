# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return []
        ret = []
        ret.extend( self.postorderTraversal(root.left))
        ret.extend( self.postorderTraversal(root.right))
        ret.append(root.val)
        return ret