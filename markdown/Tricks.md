- 204.Count the number of prime numbers less than a non-negative number, n.

计算小于n的正整数的素数的个数，只要计算2:n**0.5内的数就可以。

- 402. Given a non-negative integer *num* represented as a string, remove *k* digits from the number so that the new number is the smallest possible.

       **Note:**

       - The length of *num* is less than 10002 and will be ≥ *k*.
       - The given *num* does not contain any leading zero.

       **Example 1:**

       ```
       Input: num = "1432219", k = 3
       Output: "1219"
       Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

       ```

       **Example 2:**

       ```
       Input: num = "10200", k = 1
       Output: "200"
       Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

       ```

       **Example 3:**

       ```
       Input: num = "10", k = 2
       Output: "0"
       Explanation: Remove all the digits from the number and it is left with nothing which is 0.
       ```

首先删除跳变最大的值，即这个数比右边的数大。每删除一个k-1.此时，字符串内数字应该按升序排列。若遍历完k仍然大于0，则删除末尾的k个数。

- 3.题目：计算一个数的二进制中，1的个数

*把一个整数减1，再与原来的数做位与运算，得到的结果相当于把这个整数的二进制表示中，最右边的一个1变成了0.

- 题目：判断一个数是不是二的整数次方

*如果一个数是二的整数次方，那么他的二进制表示中有且只有一位是1

- [48. Rotate Image](https://leetcode.com/problems/rotate-image/#/description)

  旋转问题通用解题方法:

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

python使用向下取整。因此 -2 / 5 = -1

需要单独判断负数的情况。