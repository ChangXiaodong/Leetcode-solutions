def find_max_array_cross_middle(A, left, right):
    left_sum = 0
    left_index = 0
    sum = 0

    middle = int((left + right) / 2)
    for i in range(middle, left, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            left_index = i
    sum = 0
    right_sum = 0
    right_index = 0
    for i in range(middle + 1, right):
        sum += A[i]
        if sum > right_sum:
            right_sum = sum
            right_index = i

    return left_index, right_index, left_sum + right_sum


def find_max_array(A, left, right):
    if left == right:
        return left, right, A[left]
    else:
        middle = int((left + right) / 2)
        left_low_index, left_high_index, left_sum = find_max_array(A, left, middle)
        right_low_index, right_high_index, right_sum = find_max_array(A, middle + 1, right)
        cross_low_index, cross_high_index, cross_sum = find_max_array_cross_middle(A, left, right)
        if left_sum > right_sum and left_sum > cross_sum:
            return left_low_index, left_high_index, left_sum
        elif right_sum > left_sum and right_sum > cross_sum:
            return right_low_index, right_high_index, right_sum
        else:
            return cross_low_index, cross_high_index, cross_sum


def find_max_sub_array_liner(ary):
    right = 0
    sum_buf = 0
    max_sum = 0
    arr_length = 0
    for i, v in enumerate(ary):
        sum_buf += v
        arr_length += 1
        if sum_buf > max_sum:
            max_sum = sum_buf
            right = i
        if sum_buf < 0:
            sum_buf = 0
            arr_length = 0
    return right - arr_length - 1, right, max_sum

if __name__ == "__main__":
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -222, 15, 50, -100]
    print(find_max_sub_array_liner(A))
    print(find_max_array(A, 0, len(A) - 1))
