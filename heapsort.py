import time
import random

def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def heaps(array):
    n = len(array)


    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    return array


if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7] #for testing
    print("Original array:", array)
    heaps(array)
    print("Sorted array:", array)

#for Comparison
# Merge Sort Implementation
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array

# Quicksort Implementation
def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = random.choice(array) #picking a random pivot for this testing
    less = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]
    return quicksort(less) + equal + quicksort(greater)

# test cases
def testCases(size):
    randomArray = [random.randint(0, size) for _ in range(size)]
    sortedArray = list(range(size))
    reverseArray = list(range(size, 0, -1))
    return randomArray, sortedArray, reverseArray

def executionTime(array, sorting_func):
    start_time = time.time()
    sorting_func(array.copy())
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    sizes = [1000, 5000, 10000]
    for Z in sizes:
        print(f"\nArray size: {Z}")
        randomArray, sortedArray, reverseArray = testCases(Z)

        # Testing Heapsort
        print("\nHeapsort:")
        print(f"Random Array Time: {executionTime(randomArray, heaps):.5f} seconds")
        print(f"Sorted Array Time: {executionTime(sortedArray, heaps):.5f} seconds")
        print(f"Reverse Array Time: {executionTime(reverseArray, heaps):.5f} seconds")

        # Testing Quicksort
        print("\nQuicksort:")
        print(f"Random Array Time: {executionTime(randomArray, quicksort):.5f} seconds")
        print(f"Sorted Array Time: {executionTime(sortedArray, quicksort):.5f} seconds")
        print(f"Reverse Array Time: {executionTime(reverseArray, quicksort):.5f} seconds")

        # Testing Merge Sort
        print("\nMerge Sort:")
        print(f"Random Array Time: {executionTime(randomArray, merge_sort):.5f} seconds")
        print(f"Sorted Array Time: {executionTime(sortedArray, merge_sort):.5f} seconds")
        print(f"Reverse Array Time: {executionTime(reverseArray, merge_sort):.5f} seconds")

