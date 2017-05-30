def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        max_area = max((right - left) * min(height[left], height[right]),max_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area



print(maxArea([1, 2, 1]))
