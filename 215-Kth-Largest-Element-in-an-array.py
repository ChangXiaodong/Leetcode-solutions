def findkthLatgest(nums, k):
    if not nums:
        return 0
    n = len(nums)
    k = n - k

    def swap(i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def find(left, right):
        index = left + 1
        pivot = nums[left]
        for i in range(left+1, right+1):
            if nums[i] <= pivot:
                swap(i, index)
                index += 1
        index -= 1
        swap(left, index)
        if index == k:
            return nums[k]
        elif index < k:
            return find(index + 1, right)
        else:
            return find(left, index - 1)

    return find(0, n - 1)


print findkthLatgest([3,2,1,5,6,4], 2)
