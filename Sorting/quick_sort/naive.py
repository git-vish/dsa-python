from typing import List


def sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr

    # pick middle element as pivot
    mid = len(arr) // 2
    pivot = arr.pop(mid)

    left = []
    right = []

    for num in arr:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return sort(left) + [pivot] + sort(right)


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    array = sort(array)
    print(' '.join([str(x) for x in array]))
