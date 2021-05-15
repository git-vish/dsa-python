from typing import List


def search(arr: List[int], key: int) -> int:
    if not arr:
        return -1

    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left+right)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid-1
    return -1


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    x = int(input())
    print(search(array, x))
