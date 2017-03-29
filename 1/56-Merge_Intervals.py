# coding=utf-8
'''
先对每个interval的start排序。对排序后的intrevals遍历。start，end存储当前的上下界
对遍历到的上下界分别进行判断。
s大于end或e小于start，说明没有区间重复，直接添加新区间
s>=start and e>end， 新end比原end大，更新原end
同理寻中续建重复性

'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        start = float('-inf')
        end = float("-inf")
        res = []
        arr = []
        for inter in intervals:
            arr.append([inter.start, inter.end])
        arr = sorted(arr, key=lambda x: x[0])
        for s, e in arr:
            if s > end or e < start:
                start = s
                end = e
                res.append([start, end])
            elif s >= start and e > end:
                res.pop()
                end = e
                res.append([start, end])
            elif s < start and e <= end:
                res.pop()
                start = s
                res.append([start, end])
            elif s < start and e > end:
                res.pop()
                start = s
                end = e
                res.append([start, end])
        return res

