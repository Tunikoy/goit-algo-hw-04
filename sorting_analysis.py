import timeit
import random
import matplotlib.pyplot as plt
import pandas as pd

# Implementing Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Implementing Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Generate random lists for benchmarking
def generate_random_list(size):
    return [random.randint(1, 10000) for _ in range(size)]

# List sizes for comparison
sizes = [100, 1000, 5000]

# Compare algorithms on different list sizes using timeit
results = []

for size in sizes:
    data = generate_random_list(size)
    
    # Time each sorting algorithm using timeit
    merge_time = timeit.timeit('merge_sort(data.copy())', setup='from __main__ import merge_sort, data', number=10)
    insertion_time = timeit.timeit('insertion_sort(data.copy())', setup='from __main__ import insertion_sort, data', number=10)
    timsort_time = timeit.timeit('sorted(data.copy())', setup='from __main__ import data', number=10)

    results.append({
        "Size": size,
        "Merge Sort": merge_time,
        "Insertion Sort": insertion_time,
        "Timsort": timsort_time
    })

results_df = pd.DataFrame(results)

# Save results to CSV
results_df.to_csv('results.csv', index=False)

# Visualization of the results
def plot_sorting_results(df):
    plt.figure(figsize=(10, 6))
    
    # Plotting each sorting algorithm
    plt.plot(df['Size'], df['Merge Sort'], label='Merge Sort', marker='o')
    plt.plot(df['Size'], df['Insertion Sort'], label='Insertion Sort', marker='o')
    plt.plot(df['Size'], df['Timsort'], label='Timsort (built-in)', marker='o')
    
    # Adding labels and legend
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Sorting Algorithms by Execution Time')
    plt.legend()
    plt.grid(True)
    
    # Save the plot to a file
    plt.savefig('sorting_comparison.png')
    plt.show()

plot_sorting_results(results_df)

#a1234@Macmini goit-algo-hw-04 % python3.12 /Users/a1234/goit-algo-hw-04/sorting_analysis.py