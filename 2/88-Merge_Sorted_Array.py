#codinf=utf-8
'''
方法1：两个list从后至前比较，大的一个放在末尾
方法2：将nums2从头至尾与nums1比较，若大于则插入1，小于则将nums1之后后移
'''
def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    index = 0
    for i in range(n):
        if i >= m:
            nums1.insert(index, nums2[i])
            index += 1
            m += 1
            nums1.pop()
        else:
            while index < m and nums2[i] > nums1[index]:
                index += 1
            nums1.insert(index, nums2[i])
            m += 1
            nums1.pop()
    return nums1

def merge1(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]
    return nums1

print(merge1([2, 3, 4, 0, 0, 0, 0, 0], 3, [1, 2, 3, 4, 5], 5))
