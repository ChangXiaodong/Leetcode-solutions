'''
方法1：新建一个数组，找到坐标对应关系，完整翻转
方法2：inplace
顺时针旋转:

  ```
   * first reverse up to down, then swap the symmetry matrix[i][j] <=> matrix[j][i]
   * 1 2 3     7 8 9     7 4 1
   * 4 5 6  => 4 5 6  => 8 5 2
   * 7 8 9     1 2 3     9 6 3
  ```

  逆时针旋转：

  ```
   * first reverse left to right, then swap the symmetry matrix[i][j] <=> matrix[j][i]
   * 1 2 3     3 2 1     3 6 9
   * 4 5 6  => 6 5 4  => 2 5 8
   * 7 8 9     9 8 7     1 4 7
  ```
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        n = matrix.__len__()
        rotate = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotate[j][n-1-i] = matrix[i][j]
        matrix[:] = rotate[:]

    def rotate1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        n = matrix.__len__()
        matrix.reverse()
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a.reverse()
print(a)
