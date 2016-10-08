# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:
        	return False
        fast,slow = head,head
        while fast!=None:
        	if fast.next!=None and fast.next.next!=None:
        		fast = fast.next.next
        	else:
        		return False
        	slow = slow.next
        	if fast==slow: return True
        return False


x1=ListNode(1)
so = Solution()
print so.hasCycle(x1)
