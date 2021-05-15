from typing import List


def sort(arr: List[int]) -> None:
    if len(arr) < 2:
        return

    for i in range(0, len(arr) - 1):
        min_ = 999999  # upper bound
        idx = -1
        for j in range(i, len(arr) - 1):
            if arr[j] < min_:
                min_ = arr[j]
                idx = j

        temp = arr[i]
        arr[i] = arr[idx]
        arr[idx] = temp


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    sort(array)
    print(' '.join([str(x) for x in array]))
