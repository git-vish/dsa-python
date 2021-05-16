from typing import List


def merge(arr_1: List[int], arr_2: List[int]) -> List[int]:
    result = []
    i, j = 0, 0

    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] <= arr_2[j]:
            result.append(arr_1[i])
            i += 1
        else:
            result.append(arr_2[j])
            j += 1

    while i < len(arr_1):
        result.append(arr_1[i])
        i += 1

    while j < len(arr_2):
        result.append(arr_2[j])
        j += 1

    return result


def sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = sort(left_arr)
    right_arr = sort(right_arr)

    return merge(left_arr, right_arr)


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    array = sort(array)
    print(' '.join([str(x) for x in array]))
