import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def benchmark_sorting_algorithm(sort_function, arr_sizes):
    times = []
    for size in arr_sizes:
        arr = random.sample(range(size * 10), size)
        start_time = time.time()
        sort_function(arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

arr_sizes = [5, 10, 20, 50, 100, 200, 500, 1000]

insertion_times = benchmark_sorting_algorithm(insertion_sort, arr_sizes)
selection_times = benchmark_sorting_algorithm(selection_sort, arr_sizes)
bubble_times = benchmark_sorting_algorithm(bubble_sort, arr_sizes)

print("Array Size | Insertion Sort Time (seconds) | Selection Sort Time (seconds) | Bubble Sort Time (seconds)")
for i, size in enumerate(arr_sizes):
    print(f"{size:10} | {insertion_times[i]:.6f} | {selection_times[i]:.6f} | {bubble_times[i]:.6f}")