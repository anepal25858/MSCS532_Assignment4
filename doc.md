Heapsort Implementation and Analysis

1. Implementation
Please review heapsort.py to see the implementation of the Heapsort algorithm.
The code also consist a comparison between heapsort, mergesort and quicksort.

2. Analysis
-Best Case
The heapification and extraction process occurs as usual in the best case scenario which is already sorted data.
So, the time complexity is O(nlogn)
-Worst Case
Since Heapsort does not depend on the ordering of the array, the worst case is also O(nlogn)
-Average Case
Because of the consistence and the maintenance of the heap, the average case scenario is also same as best and
worst case scenario: O(nlogn)
Space Complexity: O(log n), due to the recursive call stack.
However, auxiliary space can be O(1) for iterative implementation.
[ Reference: greekforgreek.org]

3. Comparison
In the code, a comparison is done between different sort in different input sizes
-Heapsort: Perform consistently across all input types, including sorted, reverse-sorted, and random arrays.
-Quicksort: Perform faster on average than Heapsort for random arrays but poorly on already sorted arrays unless randomized.
-Merge Sort: Performs consistently for all input types. Perform a little faster than heapsort.

Heapsort is efficient and consistent across all input types. It is better that quicksort in the worst case scenario and
is comparable to mergesort.


Priority Queue Implementation and Applications

1. Data Structure
For this part of the code, I have used an array for implementing a binary heap.
A binary heap can be easily represented as an array where the parent and children relationships can be derived
using index calculation.
Heap operations are simple to implement using array.
I have implemented max-heap since it gives priority to tasks with higher value.
This is suitable for algorithms that prioritize the most important tasks first.
def __lt__(self, other):
        return self.priority < other.priority

2. Core Operation
Please review priorityQueue.py for the implementation.

-insert(task)
Time complexity of this operation is O(log n), where n is the number of elements, because the task needs to move up
to the root in worst case scenario.

-extract_max/min()
Time complexity of this operation is also O(log n), because in worst case scenario the task need to move up/down
to a leaf node.

-increase/decrease_key(task, new_priority)
Time complexity of this operation is also O(log n), because the task mae need to move to the root for increase,
and move to the leaf node for decrease.
In the code heapify_up / heapify_down function has been used.

-is_empty()
Time complexity of this operation is O(1), since it simple checks for the elements in the heap.

