class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l_stack, self.r_stack = [], []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.l_stack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.r_stack:
            self.r_stack.pop()
        elif self.l_stack:
            while self.l_stack:
                self.r_stack.append( self.l_stack.pop())
            self.r_stack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if self.r_stack:
            return self.r_stack[-1]
        if self.l_stack:
            while  self.l_stack:
                self.r_stack.append( self.l_stack.pop())
            return self.r_stack[-1]
        return None
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.r_stack!=[] or self.l_stack!=[]:
            return False
        else:
            return True

so=Queue()
so.push(1)
so.push(2)
so.push(3)
print so.peek()
so.pop()
print so.peek()
so.push(4)
print so.peek()
so.push(5)
print so.peek()
so.pop()

print so.peek()
so.pop()
print so.peek()
print so.empty()

