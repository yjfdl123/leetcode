class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        small,big = self.get_min_max_path(root)
        return big-small<=1

    def get_min_max_path(self,root):
    	if root==None:
    		return 0,0
    	lmin,lmax = self.get_min_max_path(root.left)
    	rmin,rmax = self.get_min_max_path(root.right)
    	return min(lmin,rmin)+1,max(lmax,rmax)+1