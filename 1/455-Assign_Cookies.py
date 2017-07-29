def findContentChildren(g, s):
    g = sorted(g)
    s = sorted(s)
    content_num = 0
    g_point = 0
    s_point = 0
    while g_point < len(g) and s_point < len(s):
        if s[s_point] >= g[g_point]:
            g_point += 1
            s_point += 1
            content_num += 1
        else:
            s_point += 1
    return content_num


print(findContentChildren([1, 2, 2], [1, 2, 1]))
