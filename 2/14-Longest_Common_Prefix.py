#coding=utf-8
'''
垂直搜索
水平搜索
二叉树搜索
分治法
'''
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    common_str = strs[0]
    common_len = len(common_str)
    n = strs.__len__()
    for i in range(1, n):
        cur_str_n = len(strs[i])
        for j in range(common_len):
            if j < cur_str_n:
                if strs[i][j] != common_str[j]:
                    common_str = strs[i][:j]
                    common_len = j
                    break
            else:
                common_str = strs[i][:j]
                common_len = j
                break
    print(type(common_str))
    return common_str


print(longestCommonPrefix(["a", "b"]))
