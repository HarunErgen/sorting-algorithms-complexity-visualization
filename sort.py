from random import randint

# Comparison Sorts
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array.pop(randint(0,len(array)-1))
    elements_greater = []
    elements_smaller = []
    for e in array:
        if e > pivot:
            elements_greater.append(e)
        else:
            elements_smaller.append(e)
    return quick_sort(elements_smaller) + [pivot] + quick_sort(elements_greater)

def merge_sort(array):
    if len(array) <= 1:
        pass
    else:    
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]
        merge_sort(left_array)
        merge_sort(right_array)
        merge(left_array, right_array, array)
def merge(array_1, array_2, arr):
    len_1, len_2 = len(array_1), len(array_2)
    i = j = k = 0
    while i < len_1 and j < len_2:
        if array_1[i] <= array_2[j]:
            arr[k] = array_1[i]
            i += 1
        else:
            arr[k] = array_2[j]
            j += 1
        k += 1
    while i < len_1:
        arr[k] = array_1[i]
        i += 1
        k += 1
    while j < len_2:
        arr[k] = array_2[j]
        j += 1
        k += 1

def heap_sort(array): 
    size = len(array)
    for i in range(size//2, -1, -1):
        heapify(array, size, i)
    for i in range(size-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
def heapify(arr, n, parent_index):
    max_index = parent_index
    left = 2 * parent_index + 1
    right = 2 * parent_index + 2
    if left < n and arr[parent_index] < arr[left]:
        max_index = left
    if right < n and arr[max_index] < arr[right]:
        max_index = right
    if max_index != parent_index:
        arr[parent_index], arr[max_index] = arr[max_index], arr[parent_index]
        heapify(arr, n, max_index)

# Non-comparison Sorts
def lsd_radix_sort(array):
    BASE = 10
    buckets = [[] for i in range(BASE)]
    max_length = False
    tmp = -1
    placement = 1
    while not max_length:
        max_length = True
        for e in array:
            tmp = e // placement
            buckets[tmp % BASE].append(e)
            if max_length and tmp > 0:
                max_length = False
        i = 0
        for bucket in buckets:
            for e in bucket:
                array[i] = e
                i += 1
            bucket.clear()
        placement *= BASE

def counting_sort(array):
    max_element = max(array)
    count_array = [0 for _ in range(max_element+1)]
    output_array = [0 for _ in range(len(array))]
    for element in array:
        count_array[element] += 1
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i-1]
    for i in range(len(array)-1,-1,-1):
        element = array[i]
        count_array[element] -= 1
        new_position = count_array[element]
        output_array[new_position] = element
    return output_array
