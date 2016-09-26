# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
        	return None
        len1, len2 = 0, 0
        h1,h2 = headA,headB
        while h1:
        	len1+=1
        	h1 = h1.next
        while h2:
        	len2+=1
        	h2 = h2.next
        h1,h2 = headA, headB
        if len1<len2:
        	h1,h2 =headB ,headA
        	len1, len2 = len1, len2
        while len1>len2:
        	len1-=1
        	print h1.val
        	h1=h1.next
        while len1>0:
        	if h1==h2:
        		return h1
        	else:
        		len1-=1
        		h1,h2  = h1.next, h2.next
        return None

def convert_a_list(lst):
	head = None
	nextnode,prevnode = None, None
	for idx,item in enumerate(lst):
		if idx==0:
			prevnode = ListNode(item)
			head = prevnode
		else:
			prevnode.next = ListNode(item)
			prevnode = prevnode.next
	return head

def printlist(head):
	while head:
		print head.val
		head=head.next

if __name__ == '__main__':
	x=[1,3,5,7,9,11,13,15,17,19,21]
	y=[2,3,19,21]
	h1 = convert_a_list(x)
	h2 = convert_a_list(y)
	# printlist(h1)
	# printlist(h2)
	so =Solution()
	print so.getIntersectionNode(h1,h2)
