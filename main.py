import sort
import random
import matplotlib.pyplot as plt
from numpy import average
from time import time

base_array =  [i for i in range(0, 100000)]
array = base_array.copy()

random.seed(10)
random.shuffle(array)

quick_sort_time, merge_sort_time, heap_sort_time, lsd_radix_sort_time, counting_sort_time = [],[],[],[],[]

def handle_time_data(sort_function, array, time_data):
    start = time()
    sort_function(array)
    end = time()
    time_data.append((end - start)*1000)

for i in range(1, len(array), 10):
    handle_time_data(sort.quick_sort, array[:i], quick_sort_time)
    handle_time_data(sort.merge_sort, array[:i], merge_sort_time)
    handle_time_data(sort.heap_sort, array[:i], heap_sort_time)
    handle_time_data(sort.lsd_radix_sort, array[:i], lsd_radix_sort_time)
    handle_time_data(sort.counting_sort, array[:i], counting_sort_time)

plt.xlabel("Array Size")
plt.ylabel("Time (ms)")

plt.plot(base_array[1::10], quick_sort_time, label=f"Quick Sort. Average: {'%.2f'%average(quick_sort_time)} ms", linewidth=2)
plt.plot(base_array[1::10], merge_sort_time, label=f"Merge Sort. Average: {'%.2f'%average(merge_sort_time)} ms", linewidth=2)
plt.plot(base_array[1::10], heap_sort_time, label=f"Heap Sort. Average: {'%.2f'%average(heap_sort_time)} ms", linewidth=2)
plt.plot(base_array[1::10], lsd_radix_sort_time, label=f"LSD Radix Sort (Base 10). Average: {'%.2f'%average(lsd_radix_sort_time)} ms", linewidth=2)
plt.plot(base_array[1::10], counting_sort_time, label=f"Counting Sort. Average: {'%.2f'%average(counting_sort_time)} ms", linewidth=2)
plt.legend()

plt.show()
