def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def test_sorting_algorithm(sort_func):
    test_cases = [
        ([]),
        ([5]),
        ([1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1]),
        ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),
        ([7, -2, 10, 0, 3, 8, -5, 4]),
        ([-10, -3, 0, 5, -7, 2, 9, -1]),
        ([4, 4, 4, 4, 4]),
        ([1000000, 999999, 123456, 789012]),
        ([-999999999, 0, 999999999])
    ]

    for i, (input_arr) in enumerate(test_cases):
        result = sort_func(input_arr)
        print(result)        

test_sorting_algorithm(quicksort)

