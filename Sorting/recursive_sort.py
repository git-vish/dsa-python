from typing import List


def insert(arr: List[int], n: int) -> None:
    if len(arr) == 0 or arr[-1] <= n:
        arr.append(n)
        return
    temp = arr.pop()
    insert(arr, n)
    arr.append(temp)


def sort(arr: List[int]) -> None:
    if len(arr) <= 1:
        return

    temp = arr.pop()
    sort(arr)
    insert(arr, temp)


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    sort(array)
    print(' '.join([str(x) for x in array]))
