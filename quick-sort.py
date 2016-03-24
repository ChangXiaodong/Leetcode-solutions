def qsort(nums):
    n = len(nums)

    def swap(i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def partition(p, r):  # end as pivot
        x = nums[r]
        i = p
        for j in range(p, r):
            if nums[j] <= x:
                swap(i, j)
                i += 1
        swap(i, r)
        return i

    def patition_head(p, r):
        x = nums[p]
        i = p + 1
        for j in range(p + 1, r + 1):
            if nums[j] <= x:
                swap(i, j)
                i += 1

        swap(i - 1, p)
        return i - 1

    def quicksort(p, r):
        if p < r:
            q = patition_head(p, r)
            quicksort(p, q - 1)
            quicksort(q + 1, r)
        return nums

    print quicksort(0, n - 1)


qsort([5, 1, 2, 4, 8, 6, 5])
