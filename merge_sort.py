def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Ділимо масив навпіл
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    # Зливаємо дві половини
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    # Порівнюємо елементи і додаємо менші
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Додаємо залишки
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

def test_sorting_algorithm(sort_func):
    test_arrays = [
        [],                          # порожній
        [5],                        # один елемент
        [3, 1, 4, 1, 5, 9, 2, 6],   # невідсортований
        [1, 2, 3, 4, 5],            # вже відсортований
        [5, 4, 3, 2, 1],            # зворотньо відсортований
        [3, 3, 3, 3],               # однакові елементи
        [-5, 0, 3, -2, 1]           # від'ємні числа
    ]

    for arr in test_arrays:
        print(f"Before: {arr}")
        print(f"After : {merge_sort(arr)}")
        print("---")

test_sorting_algorithm(merge_sort)