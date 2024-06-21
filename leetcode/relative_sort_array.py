from typing import List


def relative_sort_array(arr1: List[int], arr2: List[int]) -> List[int]:
    for i in arr2:
        arr1.remove(i)

    result = arr2.copy()
    result1 = []

    for i in arr1:
        if i in arr2:
            result.insert(arr2.index(i), i)
        else:
            result1.append(i)
    return result + sorted(result1)


print(relative_sort_array([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))
