- 204.Count the number of prime numbers less than a non-negative number, n.

计算小于n的正整数的素数的个数，只要计算2:n**0.5内的数就可以。

- 402. Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible

首先删除跳变最大的值，即这个数比右边的数大。每删除一个k-1.此时，字符串内数字应该按升序排列。若遍历完k仍然大于0，则删除末尾的k个数。

- 3.题目：计算一个数的二进制中，1的个数

*把一个整数减1，再与原来的数做位与运算，得到的结果相当于把这个整数的二进制表示中，最右边的一个1变成了0.

- 题目：判断一个数是不是二的整数次方

*如果一个数是二的整数次方，那么他的二进制表示中有且只有一位是1