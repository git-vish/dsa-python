from typing import List


def search(arr: List[int], left: int, right: int, key: int) -> int:
    if left > right:
        return -1

    mid = (left+right)//2

    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return search(arr, mid+1, right, key)
    else:
        return search(arr, left, mid-1, key)


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    x = int(input())
    print(search(array, 0, len(array)-1, x))
