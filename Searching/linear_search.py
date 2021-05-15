from typing import List


def search(arr: List[int], key: int) -> int:
    for idx, num in enumerate(arr):
        if num == key:
            return idx
    return -1


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    x = int(input())
    print(search(array, x))
