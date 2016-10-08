# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        num,node = self.numfind(root,p,q)
        if num==2:
            return node
        else:
            return None

    def numfind(self,root,p,q):
        print root,root.val
        if root is None:
            return 0,None
        lnum,rnum = 0,0
        lnum,node = self.numfind(root.left,p,q)
        if lnum==2: return lnum,node
        rnum,node = self.numfind(root.right,p,q)
        if rnum==2: return rnum,node
        if root==p or root==q:
            pnum=1
        pnum += lnum + rnum
        if pnum==2: return pnum,root


class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        print root
        if root is None:
            return None
            
        if root is A or root is B:
            return root
            
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        
        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        if right is not None:
            return right
        return None

x1=TreeNode(1)
x2=TreeNode(2)
x1.left = x2
so=Solution()
print so.lowestCommonAncestor(x1,x1,x2)