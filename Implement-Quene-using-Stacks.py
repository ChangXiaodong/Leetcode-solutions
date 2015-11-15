__author__ = 'Changxiaodong'
import time
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.quene = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        buf = []
        for items in self.quene:
            buf.append(items)
        self.quene = []
        self.quene.append(x)

        for items in buf:
            self.quene.append(items)


    def pop(self):
        """
        :rtype: nothing
        """
        self.quene.pop()


    def peek(self):
        """
        :rtype: int
        """
        return self.quene[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.quene) == 0

if __name__ == "__main__":
    start = time.clock()
    test = Queue()
    test.push(1)
    print test.peek()
    print time.clock() - start