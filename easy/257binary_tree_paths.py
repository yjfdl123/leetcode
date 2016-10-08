import sys
sys.path.append('..')
from  data_structure import binarytree
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
    	print root
    	print root.val
    	print root.left
    	print root.right
    	if root ==None:
    		return []
    	else:
    		print 1222112
		ret=[]    	
		print "sd"
		self.findpath(root,"",ret)
		res = [path[:-3] for path in ret]
		return res

    def findpath(self,root,path,plst):
    	print path
    	if root==None:
    		plst.append(path)
    	else:
    		self.findpath(root.left,  path+str(root.val)+"->",plst)
    		self.findpath(root.right, path+str(root.val)+"->",plst)

gen = binarytree.BinaryTree()
tree = gen.create_tree([1,None,3,None,5])
gen.print_tree(tree)
so = Solution()
print so.binaryTreePaths(tree)


