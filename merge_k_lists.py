import heapq

def merge_k_lists(lists):
    min_heap = []
    for lst in lists:
        for num in lst:
            heapq.heappush(min_heap, num)

    sorted_list = [heapq.heappop(min_heap) for _ in range(len(min_heap))]
    return sorted_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
