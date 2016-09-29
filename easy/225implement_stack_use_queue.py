class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l_queue, self.r_queue = [], []
    

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.l_queue.append(x)
        

    def transfer(self):
        if not self.l_queue: 
            self.l_queue, self.r_queue = self.r_queue, self.l_queue
        while len(self.l_queue)>1:
            self.r_queue.append( self.l_queue[0])
            self.l_queue.remove( self.l_queue[0])
    def pop(self):
        """
        :rtype: nothing
        """
        self.transfer()
        self.l_queue = []

    def top(self):
        """
        :rtype: int
        """
        self.transfer()
        if len(self.l_queue)>0:
            return self.l_queue[0]
        else:
            return None

        

    def empty(self):
        """
        :rtype: bool
        """
        if self.l_queue==[] and self.r_queue==[]:
            return True
        else:
            return False

x=[1,2,3]
x.remove(x[0])
print x

