#coding=utf-8
'''
方法1:每一行进行遍历
每一行内用二分查找

方法二：从右上角开始搜索。
如果target比右上角元素小，则target不可能在右上角这一列
如果target比右上角元素大，则target不可能在右上角这一行
根据这个特征更新rowindex和colindex
'''
def bs(nums, x):
    if not nums:
        return False
    low = 0
    high = nums.__len__() - 1
    while low <= high:
        mid = (low + high) // 2
        if x < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
        if nums[mid] == x:
            return True
    return False

def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix:
        return False
    for row in matrix:
        if bs(row, target):
            return True
    return False


def searchMatrix1(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix:
        return False
    col = len(matrix[0]) - 1
    row = len(matrix)
    row_index = 0
    while row_index < row and col >= 0:
        if target > matrix[row_index][col]:
            row_index += 1
        elif target < matrix[row_index][col]:
            col -= 1
        else:
            return True
    return False