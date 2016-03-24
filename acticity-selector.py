def recursive_activity_selector(s, f, k, n, activity):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m += 1
    if m <= n:
        activity.append(m)
        recursive_activity_selector(s, f, m, n, activity)


def greedy_activity_selector(s, f):
    activity = []
    n = len(s)
    activity.append(1)
    k = 1
    for m in range(2, n):
        if s[m] >= f[k]:
            activity.append(m)
            k = m
    return activity


a = []
s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
recursive_activity_selector(s, f, 0, 11, a)
print a
print greedy_activity_selector(s, f)
