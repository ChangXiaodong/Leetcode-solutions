# coding=utf-8
'''
维护两个列表，一个列表（course）存这个课需要那些先修课程，另一个（pre_course）存这个课是哪些课的先修课程。(这个表是为了提升查找速度)
首先找到不需要先修课程的这门课。如果不存在就说明无法完成。在pre_course中找到这个能够修的课是哪些课的先修课程，这个课已经学会，添加到res中
并在course中需要这门课的对应课程中删除这门课。然后再看course是否有先修课程为空的课程。如果没有，检查res是否修完了所有课程。修完了所有课程则返回结果
否则无法完成
'''
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        course = [[] for _ in range(numCourses)]
        pre_course = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            course[cur].append(pre)
            pre_course[pre].append(cur)
        res = []
        stack = [c for c in range(numCourses) if not course[c]]
        while stack:
            c = stack.pop()
            res.append(c)
            for i in pre_course[c]:
                course[i].remove(c)
                if not course[i]:
                    stack.append(i)
        return res if res.__len__() == numCourses else []


solution = Solution()
print(solution.findOrder(4,[[0,1],[3,1],[1,3],[3,2]]))
