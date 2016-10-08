# Definition for a  binary tree cur
# class Treecur(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: Treecur
        """
        self.root = root
        self.cur_node =root
        self.path = [root]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.findnext(self.cur_node)!=None:
            return True
        else:
            return False

    def findnext(self):
        if self.cur_node.right!=None:
            child = self.cur_node.right
            if child.left==None:  
                return child
            else:
                while child.left!=None: child=child.left
                return child


    def next(self):
        """
        :rtype: int
        """
        if self.cur_node.right!=None:
            child = self.cur_node.right
            if child.left==None:  
                return child
            else:
                while child.left!=None: child=child.left
                return child
            

        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())