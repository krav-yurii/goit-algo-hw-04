import timeit
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def tim_sort(arr):
    return sorted(arr)

def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]


sizes = [100, 1000, 10000]

for size in sizes:
    arr = generate_random_list(size)
    
    print(f"\nПорівняння для масиву з {size} елементів:")

    merge_sort_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
    print(f"Час сортування злиттям: {merge_sort_time:.5f} секунд")

    insertion_sort_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
    print(f"Час сортування вставками: {insertion_sort_time:.5f} секунд")

    tim_sort_time = timeit.timeit(lambda: tim_sort(arr.copy()), number=1)
    print(f"Час Timsort: {tim_sort_time:.5f} секунд")