class Solution(object):
    def dfs(self, course, cur_cour, learned, sch):
        pre_cour = course[cur_cour]
        for cour in pre_cour:
            if not cour in learned:
                if cour in sch:
                    return False
                sch.append(cour)
                learned.append(cour)
                self.dfs(course, cour, learned, sch)
        self.path.append(cur_cour)
        return True

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        course = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            course[cur].append(pre)
        self.path = []
        for cur, pre in prerequisites:
            p = self.dfs(course, cur, [],[])
            if not p:
                return []
        return self.path


solution = Solution()
print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

