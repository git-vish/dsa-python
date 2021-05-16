from typing import List


def sort(arr: List[int]) -> None:
    if len(arr) < 2:
        return

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    sort(array)
    print(' '.join([str(x) for x in array]))
