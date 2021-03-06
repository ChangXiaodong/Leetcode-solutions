# KMP算法

解决子数组查找问题

有一个字符串"BBC ABCDAB ABCDABCDABDE"，判断里面是否包含另一个字符串"ABCDABD"？

Leetcode
28.Implement strStr()
```python
def strStr2(haystack, needle):
    if not haystack and not needle:
        return 0
    if not needle:
        return 0
    n1 = len(haystack)
    n2 = len(needle)
    table = [0 for _ in range(n2)]

    i = 1
    j = 0
    # build table
    while i < n2:
        if needle[i] != needle[j]:
            if j > 0:
                j = table[j - 1]
            else:
                i += 1
        else:
            table[i] = j + 1
            j += 1
            i += 1
    index1 = 0
    index2 = 0
    # search
    while index1 < n1:
        if haystack[index1] == needle[index2]:
            if index2 == n2 - 1:
                return index1 + 1 - n2
            else:
                index1 += 1
                index2 += 1
        else:
            if index2 == 0:
                index1 += 1
            else:
                index2 = table[index2 - 1] 
                #index2 = index2 - (index2 - table[index2 - 1])
    return -1
```

## 普通算法
遍历字符串str1，检查每一个字符是否与str2匹配。如果不匹配，查找str1里面下一个字符，str2的pointer重置到开头。

时间复杂度为O(m*n)

##KMP
先介绍“部分匹配表”
### 部分匹配表

首先，要了解两个概念："前缀"和"后缀"。 "前缀"指除了最后一个字符以外，一个字符串的全部头部组合；"后缀"指除了第一个字符以外，一个字符串的全部尾部组合。
　![bufenpipeibiao](./images/kmp15.png)
  "部分匹配值"就是"前缀"和"后缀"的最长的共有元素的长度。以"ABCDABD"为例，
-  "A"的前缀和后缀都为空集，共有元素的长度为0；
-  "AB"的前缀为[A]，后缀为[B]，共有元素的长度为0；
-  "ABC"的前缀为[A, AB]，后缀为[BC, C]，共有元素的长度0；
-  "ABCD"的前缀为[A, AB, ABC]，后缀为[BCD, CD, D]，共有元素的长度为0；
-  "ABCDA"的前缀为[A, AB, ABC, ABCD]，后缀为[BCDA, CDA, DA, A]，共有元素为"A"，长度为1；
-  "ABCDAB"的前缀为[A, AB, ABC, ABCD, ABCDA]，后缀为[BCDAB, CDAB, DAB, AB, B]，共有元素为"AB"，长度为2；
-  "ABCDABD"的前缀为[A, AB, ABC, ABCD, ABCDA, ABCDAB]，后缀为[BCDABD, CDABD, DABD, ABD, BD, D]，共有元素的长度为0。
    　　![kmp16](./images/kmp16.png)
    　　　"部分匹配"的实质是，有时候，字符串头部和尾部会有重复。比如，"ABCDAB"之中有两个"AB"，那么它的"部分匹配值"就是2（"AB"的长度）。搜索词移动的时候，第一个"AB"向后移动4位（字符串长度-部分匹配值），就可以来到第二个"AB"的位置。

### 匹配算法
1. 首先，字符串"BBC ABCDAB ABCDABCDABDE"的第一个字符与搜索词"ABCDABD"的第一个字符，进行比较。因为B与A不匹配，所以搜索词后移一位。
   ![kmp1](./images/kmp1.png)
2. 因为B与A不匹配，搜索词再往后移。
   ![kmp2](./images/kmp2.png)
3. 就这样，直到字符串有一个字符，与搜索词的第一个字符相同为止。
   ![kmp3](./images/kmp3.png)
4. 接着比较字符串和搜索词的下一个字符，还是相同。
   ![kmp4](./images/kmp4.png)
5. 直到字符串有一个字符，与搜索词对应的字符不相同为止。
   ![kmp5](./images/kmp5.png)
6. 这时，最自然的反应是，将搜索词整个后移一位，再从头逐个比较。这样做虽然可行，但是效率很差，因为你要把"搜索位置"移到已经比较过的位置，重比一遍。
   ![kmp6](./images/kmp6.png)
7. 一个基本事实是，当空格与D不匹配时，你其实知道前面六个字符是"ABCDAB"。KMP算法的想法是，设法利用这个已知信息，不要把"搜索位置"移回已经比较过的位置，继续把它向后移，这样就提高了效率。
   ![kmp7](./images/kmp7.png)
8. 怎么做到这一点呢？可以针对搜索词，算出一张《部分匹配表》（Partial Match Table）。
   ![kmp15](./images/kmp15.png)
9. 已知空格与D不匹配时，前面六个字符"ABCDAB"是匹配的。查表可知，最后一个匹配字符B对应的"部分匹配值"为2，因此按照下面的公式算出向后移动的位数

   移动位数 = 已匹配的字符数 - 对应的部分匹配值

   因为 6 - 2 等于4，所以将搜索词向后移动4位。
   ![kmp9](./images/kmp9.png)
10. 因为空格与Ｃ不匹配，搜索词还要继续往后移。这时，已匹配的字符数为2（"AB"），对应的"部分匹配值"为0。所以，移动位数 = 2 - 0，结果为 2，于是将搜索词向后移2位。
![kmp10](./images/kmp10.png)
11. 因为空格与A不匹配，继续后移一位。
![kmp11](./images/kmp11.png)
12. 逐位比较，直到发现C与D不匹配。于是，移动位数 = 6 - 2，继续将搜索词向后移动4位。
![kmp12](./images/kmp12.png)
13. 逐位比较，直到搜索词的最后一位，发现完全匹配，于是搜索完成。如果还要继续搜索（即找出全部匹配），移动位数 = 7 - 0，再将搜索词向后移动7位，这里就不再重复了。
![kmp13](./images/kmp13.png)

[原文链接](http://www.ruanyifeng.com/blog/2013/05/Knuth–Morris–Pratt_algorithm.html)



