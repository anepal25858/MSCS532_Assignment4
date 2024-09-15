#1 Data Structure:
#we are using array and max-heap for implementing binary heap.
#please review detail info in doc.md file

import array

class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(ID: {self.task_id}, Priority: {self.priority}, Arrival: {self.arrival_time}, Deadline: {self.deadline})"

#2 Core Operation

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            raise IndexError("Extracting from an empty priority queue")

        max_task = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_task

    def increase_key(self, task_id, new_priority):
        for index, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority > task.priority:
                    task.priority = new_priority
                    self._heapify_up(index)
                return
        raise ValueError("Task ID not found")

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index].priority > self.heap[parent_index].priority:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        size = len(self.heap)
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        if left_child < size and self.heap[left_child].priority > self.heap[largest].priority:
            largest = left_child

        if right_child < size and self.heap[right_child].priority > self.heap[largest].priority:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

# Test code
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(Task(1, 5, 100, 2024))
    pq.insert(Task(2, 3, 200, 2025))
    pq.insert(Task(3, 8, 1200, 2030))

    print("\nHeap after insertions:", pq.heap)

    pq.increase_key(2, 10)
    print("\nHeap after increasing priority of task ID 2:", pq.heap)

    max_task = pq.extract_max()
    print("\nExtracted max task:", max_task) #In this case task 2
    print("\nHeap after extracting max:", pq.heap)
