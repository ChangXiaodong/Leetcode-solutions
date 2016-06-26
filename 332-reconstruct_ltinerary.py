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


print findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])
