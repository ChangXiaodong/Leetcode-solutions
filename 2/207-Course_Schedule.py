class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        table = {}
        for course in prerequisites:
            if len(course) > 1:
                if table.get(course[0], []) == []:
                    table[course[0]] = course[1]
            else:
                table[course] = []

        for key in table:
            path = []
            path.append(table[key])
            while table.get(path[-1], []) != []:
                next_cour = table[path[-1]]
                if next_cour in path:
                    return False
                path.append(next_cour)
        return True


solution = Solution()
print(solution.canFinish(4, [[1,0],[2,1],[3,2],[1,3]]))
