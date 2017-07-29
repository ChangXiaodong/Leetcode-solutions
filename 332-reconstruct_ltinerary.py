'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
'''
def findItinerary(tickets):
    import collections
    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    route = []

    def visit(airport):
        while targets[airport]:
            visit(targets[airport].pop())
        route.append(airport)

    visit('JFK')
    return route[::-1]


# print(findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))


class Solution(object):
    def dfs(self, tickets, table, buf, _from):
        if not table:
            buf.append(_from)
            return buf
        if not table.get(_from, "null") == "null":
            buf.append(_from)
            for i in range(len(table[_from])):
                _to = table[_from][i]
                table[_from].pop(i)
                if not table[_from]:
                    del table[_from]
                if self.dfs(tickets, table, buf, _to):
                    return buf
                if table.get(_from, 'null') == "null":
                    table[_from] = []

                table[_from].insert(i, _to)

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        table = {}
        for _from, _to in tickets:
            if table.get(_from, "null") == 'null':
                table[_from] = []
            table[_from].append(_to)
        for key, value in table.items():
            table[key].sort()
        res = []
        self.dfs(tickets, table, res, "JFK")
        return res

s = Solution()
print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
