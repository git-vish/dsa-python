from typing import List


def sort(arr: List[int]) -> None:
    if len(arr) < 2:
        return

    for i in range(1, len(arr)):
        swapped = False
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        if not swapped:
            return


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    sort(array)
    print(' '.join([str(x) for x in array]))
