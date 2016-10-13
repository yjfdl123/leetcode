# Definition for singly-linked list.
import time
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smallhead,greathead=None,None
        node=head
        smallnode,greatnode=None,None
        smallprev,greatprev=None,None
        while node!=None:
            tmp=node.next
            if node.val<x:
                if smallhead==None:
                    smallhead=node
                    smallprev=node
                else:
                    smallprev.next=node
                    smallprev=node
                smallprev.next=None
            else:
                if greathead==None:
                    greathead=node
                    greatprev=node
                else:
                    greatprev.next=node
                    greatprev=node
                greatprev.next=None
            node=tmp
        if smallhead==None: return greathead
        # if greathead==None: return greathead
        smallprev.next=greathead
        return smallhead

so=Solution()
x=ListNode(2)
x.next=ListNode(1)
print so.partition(x,1)
node=x
# while node!=None:
#     print node.val