#coding=utf-8
'''
方法1：二分查找，O(nlgn*lgX)，其中X为最大值和最小值的差值
方法2：堆排序 从最小开始，每次把元素下面和右面的数推入堆，直到K个为止
'''
def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    low = matrix[0][0]
    high = matrix[-1][-1]
    n = len(matrix)
    while low < high:
        mid = (low + high) // 2
        j = n - 1
        cnt = 0
        for i in range(n):
            while j >= 0 and matrix[i][j] > mid:
                j -= 1
            cnt += j + 1
        if cnt < k:
            low = mid + 1
        else:
            high = mid
    return low

def kthSmallest1(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    import heapq
    m, n = len(matrix), len(matrix[0])
    q = [(matrix[0][0], 0, 0)]
    ans = None
    for _ in range(k):
        ans, i, j = heapq.heappop(q)
        if j == 0 and i + 1 < m:
            heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
        if j + 1 < n:
            heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
    return ans



print(kthSmallest1([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))
