from typing import List


def sort(arr: List[int]) -> None:
    gap = len(arr) // 2

    while gap > 0:
        for i in range(gap, len(arr)):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
        gap //= 2


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    sort(array)
    print(' '.join([str(x) for x in array]))
