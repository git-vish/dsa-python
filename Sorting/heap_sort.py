from typing import List
from heapq import heappush, heappop


def sort(arr: List[int]) -> None:
    min_heap = []
    for num in arr:
        heappush(min_heap, num)

    arr.clear()

    while min_heap:
        arr.append(heappop(min_heap))


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    sort(array)
    print(' '.join([str(x) for x in array]))
