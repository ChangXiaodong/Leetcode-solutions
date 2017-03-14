# coding=utf-8
'''
用一个栈：
入栈时存储当前值与最小值的差
出栈时若最小值被弹出，增更新当前的最小值
top操作时，若top值>0则说明实际值比mini大，返回mini+top
若top值<0则说明实际值比上一个mini小，即为当前的mini，返回mini

用两个栈：
一个存储数据
一个维护顺序

栈内存元组
每次操作基本单位为（x, current_min）
'''


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mini = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.mini = x
        self.stack.append(x - self.mini)
        if x < self.mini:
            self.mini = x

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if x < 0:
            # pop 出的值比mini小，则增大mini
            self.mini = self.mini - x
        if not self.stack:
            self.mini = None

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            top = self.stack[-1]
            if top > 0:
                return self.mini + top
            else:
                return self.mini

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini


class MinStack2:
    def __init__(self):
        self.q = []

    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

    def pop(self):
        self.q.pop()

    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][0]

    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][1]


ministack = MinStack()
ministack.push(2147483646)
ministack.push(2147483646)
ministack.push(2147483647)
value = (ministack.top())
ministack.pop()
value = (ministack.getMin())
ministack.pop()
value = (ministack.getMin())
ministack.pop()
ministack.push(2147483647)
value = ministack.top()
value = (ministack.getMin())
ministack.push(-2147483648)
ministack.push(-2147483648)
value = (ministack.top())
value = (ministack.getMin())
ministack.pop()
value = (ministack.getMin())
