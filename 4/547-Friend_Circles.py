# coding=utf-8
'''
广度优先搜索：跟深度优先不同，深度优先使用栈，广度优先使用队列并且不需要递归。
广度优先一般结构：
一个marked数组存储当前节点是否被访问过，如果被访问过则不能进行第二次访问。
一个队列，quene，用来报保存与当前节点连通的节点。初始化时把起始节点推入队列中。
'''


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        nums = len(M)
        res = []
        marked = [False for _ in range(nums)]
        for j in range(nums):
            if marked[j]:
                continue
            marked[j] = True
            res.append([j])
            stack = [j]
            while stack:
                s = stack.pop(0)
                for i in range(nums):
                    if s != i and M[s][i] == 1 and i not in res[-1]:
                        marked[i] = True
                        stack.append(i)
                        res[-1].append(i)
        return len(res)

    def dfs(self, M, buf, index, visited):
        for i in range(len(M)):
            if i != index and M[i][index] and not visited[i]:
                visited[i] = True
                buf.append(i)
                buf = self.dfs(M, buf, i, visited)
        return buf

    def findCircleNum1(self, M):
        res = []
        visited = [False for _ in range(len(M))]
        for i in range(len(M)):
            if not visited[i]:
                buf = [i]
                visited[i] = True
                res.append(self.dfs(M, buf, i, visited))
        return len(res)


solution = Solution()
num = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
solution.findCircleNum(num)
print(solution.findCircleNum1(num))
