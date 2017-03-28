'''
第K大的数。运用快排思想
'''
def partition(nums, left, right):
    pivot = nums[right]
    i = left - 1
    for j in range(left, right):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[right], nums[i + 1] = nums[i + 1], nums[right]
    return i + 1


def quick_sort(nums, left, right, k):
    if left < right:
        q = partition(nums, left, right)
        if q == k:
            return nums[q]
        elif q > k:
            return quick_sort(nums, left, q - 1, k)
        else:
            return quick_sort(nums, q + 1, right, k)
    return nums[left]


nums = [5, 3, 1, 5, 4, 8, 1, 2, 4]
print(quick_sort(nums, 0, nums.__len__() - 1, 6))
