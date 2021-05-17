from typing import List


def sort(arr: List[int]) -> None:
    k = max(arr)
    counter = [0 for _ in range(k + 1)]
    result = [0 for _ in range(len(arr))]

    for num in arr:
        counter[num] += 1

    for i in range(1, k + 1):
        counter[i] += counter[i - 1]

    for num in arr[::-1]:
        counter[num] -= 1
        result[counter[num]] = num

    arr[:] = result


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    sort(array)
    print(' '.join([str(x) for x in array]))
