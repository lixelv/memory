def binary(lst: list, target: int):
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2

        if lst[middle] < target:
            left = middle + 1

        elif lst[middle] > target:
            right = middle - 1

        else:
            return middle

    return None


print(binary([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
