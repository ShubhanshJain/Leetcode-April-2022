class PeekingIterator:
    def __init__(self, iterator):
        self.i = iterator
        self.peeked = False
        self.tmp = None
        

    def peek(self):
        if not self.peeked:
            self.peeked = True
            self.tmp = self.i.next()
            return self.tmp
        else:
            return self.tmp
        

    def next(self):
        if self.peeked:
            self.peeked = False
            return self.tmp
        else:
            return self.i.next()

    def hasNext(self):
        if self.peeked or self.i.hasNext():
            return True
        else:
            return False