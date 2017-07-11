__author__ = 'Changxiaodong'
'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''
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