import time
import random
import platform
import psutil

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

def benchmark_sorting_algorithms():
    algorithms = {
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Bubble Sort": bubble_sort,
    }

    input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000]
    results = {alg: [] for alg in algorithms}

    for size in input_sizes:
        arr = random.sample(range(size * 10), size)  
        for alg_name, alg_func in algorithms.items():
            arr_copy = arr.copy()  
            start_time = time.time()
            alg_func(arr_copy)
            end_time = time.time()
            results[alg_name].append(end_time - start_time)

    print("System Information:")
    print(f"CPU: {platform.processor()}")
    print(f"RAM: {psutil.virtual_memory().total / 1e9:.2f} GB")
    print("\nBenchmark Results (time in seconds):")
    print("Input Size | " + " | ".join(algorithms.keys()))
    print("-" * (12 + 20 * len(algorithms)))

    for i, size in enumerate(input_sizes):
        row = f"{size:<10} | " + " | ".join(f"{results[alg][i]:<15.6f}" for alg in algorithms)
        print(row)

benchmark_sorting_algorithms()
