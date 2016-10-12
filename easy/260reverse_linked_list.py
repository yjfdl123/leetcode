# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
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

