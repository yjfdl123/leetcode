# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        newhead=None
        newnode=None
        prevnode=None
        node=head
        while node!=None:
        	newnode=ListNode(node.val)
        	if newhead==None:
        		newhead=newnode
        		prev=newnode
        	else:
        		prev.next=newnode
        		prev=newnode
        	node=node.next
        newhead=self.reverseList(newhead)
        node,newnode=head,newhead
        while node!=None:
        	if node.val==newnode.val:
        		node,newnode = node.next,newnode.next
        	else:
        		return False
        return True

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None: return head
        prev,cur,nex=None,head,head.next
        while cur!=None:
        	cur.next=prev
        	prev=cur
        	cur=nex
        	nex=nex.next
