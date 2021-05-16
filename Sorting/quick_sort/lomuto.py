from typing import List


def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def sort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        p = partition(arr, low, high)
        sort(arr, low, p - 1)
        sort(arr, p + 1, high)


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    sort(array, 0, len(array) - 1)
    print(' '.join([str(x) for x in array]))
