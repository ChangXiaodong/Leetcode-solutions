from collections import deque
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.quene = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.quene.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        if not self.empty():
            buf = []
            for v in range(len(self.quene)-1):
                buf.append(self.quene[v])
            self.quene = buf

    def top(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self.quene[-1]
        else:
            return []

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.quene)==0:
            return True
        else:
            return False

if __name__ == "__main__":
    test = Stack()
    test.push(1)
    test.top()
    print test.empty()
    print test.quene