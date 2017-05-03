class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = {}
        for v in s:
            table[v] = table.get(v, 0) + 1
        times = {}
        for key, values in table.items():
            if times.get(values, "null") == "null":
                times[values] = []
            times[values].append(key)
        decent = sorted(times.keys())[::-1]
        res = ""
        for index in decent:
            for c in times[index]:
                res += c * index
        return res


solution = Solution()
print(solution.frequencySort("cccaaa"))
