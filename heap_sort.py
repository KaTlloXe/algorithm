def heapify(arr, n, i):
    largest = i           # Припускаємо, що корінь — найбільший
    left = 2 * i + 1      
    right = 2 * i + 2     
    
    # Якщо лівий нащадок більший за корінь
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Якщо правий нащадок більший за найбільше знайдене значення
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Якщо найбільший не корінь — міняємо місцями і рекурсивно перевіряємо піддерево
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Побудова max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Витягуємо елементи по одному
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # Переміщуємо поточний корінь у кінець
        heapify(arr, i, 0)                # Відновлюємо heap для зменшеного масиву

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
        print(f"After : {sort_func(arr)}")
        print("---")

test_sorting_algorithm(heap_sort)