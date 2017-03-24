'''
问题可以转换为寻找一个图是否有环
方法1:dfs 先统计出每个点相连的点。放在graph中。然后遍历每个点。同时维护一个visit列表，表示当前路线节点的访问状态。
0，表示该节点还没访问过，1表示已经访问过该节点，-1表示该节点正在当前的遍历路径中

方法2：bfs 先统计出每个点相连的点，同时维护一个列表，表示该课程是几个课程的前提。在这个列表中至少有一个课程的前提为0。否则一定存在环路
统计完后先遍历该列表，找到前提为0的课程，将他放入队列中。队列不为空时，每次从队列中取出对头元素，该课程表示已经完成，找到需要这个前提的课程
将他需要的课程数减1.如果为0，count加1，,并放入队列中。最终判断完成课程数count和输入是否相等。
'''
class Solution(object):
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
        return True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        n = numCourses
        graph = [[] for _ in range(n)]
        visited = [0 for _ in range(n)]
        for c in prerequisites:
            graph[c[0]].append(c[1])
        for i in range(n):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def bfs(self, numCourses, prerequisites):
        n = numCourses
        graph = [[] for _ in range(n)]
        degree = [0 for _ in range(n)]
        quene = []
        count = 0
        for c in prerequisites:
            degree[c[1]] += 1
            graph[c[0]].append(c[1])
        for i in range(n):
            if degree[i] == 0:
                quene.append(i)
                count += 1
        while len(quene) != 0:
            course = quene.pop(0)
            for c in graph[course]:
                degree[c] -= 1
                if degree[c] == 0:
                    quene.append(c)
                    count += 1
        return count == numCourses


solution = Solution()
print(solution.bfs(6, [[1, 0],[2,1],[2,3],[3,1],[4,5]]))
