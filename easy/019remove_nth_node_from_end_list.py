# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n<=0 : return head
        length = 0
        node = head
        while node!=None:
        	node=node.next
        	length+=1
        if length<n: return head
        if length==n: 
        	tmp=head
        	head=head.next
        	del tmp
        	return head
        node = head
        while length!=n+1:
        	length-=1
        	node=node.next
        tmp=node.next
        node.next=node.next.next
        del tmp
        return head

