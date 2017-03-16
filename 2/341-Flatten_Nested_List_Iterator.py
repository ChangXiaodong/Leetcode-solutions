class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        def getnested(nums, res):
            for v in nums:
                if v.isInteger():
                    res.append(v.getInteger())
                else:
                    getnested(v.getList(), res)

        self.nums = []
        self.index = 0
        getnested(nestedList, self.nums)

    def getnested(self, nums, res):
        for v in nums:
            if v.isInteger():
                res.append(v)
            else:
                self.getnested(v, res)

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.nums[self.index - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < self.nums.__len__()


nestedList = [[1,1],2,[1,1]]
i, v = NestedIterator(nestedList), []
while i.hasNext():
    v.append(i.next())
print(v)
