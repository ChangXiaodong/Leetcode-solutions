class Solution(object):
    def dfs(self, graph, cur_course, visited, res):
        if visited[cur_course] == 1:
            return True
        elif visited[cur_course] == -1:
            return False
        visited[cur_course] = -1
        for c in graph[cur_course]:
            if not self.dfs(graph, c, visited, res):
                res.pop()
                return False
            else:
                res.append(c)

        visited[cur_course] = 1
        return True

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        course = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            course[cur].append(pre)
        res = []
        for i, c in enumerate(course):
            self.dfs(course, i, visited, res)
        return res


solution = Solution()
print(solution.findOrder(2, [[0, 1]]))
