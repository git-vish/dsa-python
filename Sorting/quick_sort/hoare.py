from typing import List


def partition(arr: List[int], low: int, high: int) -> int:
    """
    NOTE: Works only if array elements are unique
    """
    pivot = arr[low]

    i = low
    j = high

    while True:
        while arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def sort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        p = partition(arr, low, high)
        sort(arr, low, p)
        sort(arr, p + 1, high)


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    sort(array, 0, len(array) - 1)
    print(' '.join([str(x) for x in array]))
