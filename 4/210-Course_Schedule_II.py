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

    # visited 数组保存了3中状态，0，未学习， -1正在检查前提课程看是否能够完成学习，1已经学会
    def dfs(self, graph, visited, course):
        if visited[course] == -1:
            return False
        elif visited[course] == 1:
            return True
        visited[course] = -1
        for j in graph[course]:
            if not self.dfs(graph, visited, j):
                return False
        visited[course] = 1
        self.res.append(course)
        return True

    def findOrder1(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        n = numCourses
        graph = [[] for _ in range(n)]
        visited = [0 for _ in range(n)]
        self.res = []
        for c in prerequisites:
            graph[c[0]].append(c[1])
        for i in range(n):
            if not self.dfs(graph, visited, i):
                return []
        return self.res


solution = Solution()
print(solution.findOrder1(4,[[1,0],[3,0],[1,2],[3,2]]))
