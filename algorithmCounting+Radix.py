import time
import random


def counting_sort(arr):
    """計數排序"""
    if not arr:  # 空列表直接返回
        return arr
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1


    count = [0] * range_of_elements
    output = [0] * len(arr)

    # 計算各數出現次數
    for num in arr:
        count[num - min_val] += 1


    for i in range(1, len(count)):
        count[i] += count[i - 1]


    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output


def radix_sort(arr):
    """基數排序"""
    if not arr:  # 空列表直接返回
        return arr
    max_val = max(arr)
    exp = 1  # 從個位開始
    n = len(arr)

    while max_val // exp > 0:
        # 當前位數的計數
        output = [0] * n
        count = [0] * 10

        # 計算各位數出現次數
        for num in arr:
            index = (num // exp) % 10
            count[index] += 1


        for i in range(1, 10):
            count[i] += count[i - 1]

        # 將原數放入正確位置
        for num in reversed(arr):
            index = (num // exp) % 10
            output[count[index] - 1] = num
            count[index] -= 1

        arr = output[:]
        exp *= 10

    return arr


# 測試兩排序法所花時間
def test_sorting_methods(nums):
    print("Original array:", nums)

    # 計數排序
    start_time = time.perf_counter()
    counting_sorted = counting_sort(nums.copy())
    counting_time = time.perf_counter() - start_time
    print(f"Counting Sort time: {counting_time:.6f} seconds")
    print("Counting Sorted array:", counting_sorted)

    # 基數排序
    start_time = time.perf_counter()
    radix_sorted = radix_sort(nums.copy())
    radix_time = time.perf_counter() - start_time
    print(f"Radix Sort time: {radix_time:.6f} seconds")
    print("Radix Sorted array:", radix_sorted)



nums = [40, 3274, 30, 52, 3961, 7033, 15, 7036, 9155, 959]
test_sorting_methods(nums)