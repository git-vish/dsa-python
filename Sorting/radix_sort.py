from typing import List


def __count_sort(arr: List[int], place: int) -> None:
    """
    Sort elements of list of integers inplace, according to the place using counting sort.
    e.g.
        array = [356, 724]
        __count_sort(arr = array, place = 1)
      -----------
        array --> [724, 356]
        as place point to digits at 1's place.
    """
    counter = [0 for _ in range(10)]
    result = [0 for _ in range(len(arr))]

    for num in arr:
        idx = (num // place) % 10
        counter[idx] += 1

    for i in range(1, 10):
        counter[i] += counter[i - 1]

    for num in arr[::-1]:
        idx = (num // place) % 10
        counter[idx] -= 1
        result[counter[idx]] = num

    arr[:] = result


def radix_sort(arr: List[int]) -> None:
    max_num = max(arr)

    digits = 0

    while max_num:
        digits += 1
        max_num //= 10

    place = 1

    while digits:
        __count_sort(arr, place)
        place *= 10
        digits -= 1


if __name__ == '__main__':
    array = [int(x) for x in input().strip().split()]
    radix_sort(array)
    print(' '.join([str(x) for x in array]))
