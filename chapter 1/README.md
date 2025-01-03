# Chapter 1:
# Topics Covered:
## Parallel and Concurrent Programming 

---

## Files and Explanation

### 1. **Data Parallelism**
**File:** `Data Parallelism.py`

Demonstrates the use of NumPy for efficient data parallel computation. The script performs element-wise addition on large arrays and measures execution time.

### 2. **Do Something**
**File:** `Do_something.py`

Contains a function `do_something` which appends random numbers to a list. This function is utilized in multiprocessing and multithreading examples.

### 3. **Message Passing**
**File:** `Message Passing.py`

Illustrates inter-process communication (IPC) using the `mpi4py` library. Process 0 sends a dictionary to Process 1, demonstrating message passing in a distributed environment.

### 4. **Multiprocessing vs Multithreading**
**File:** `Multiprocessing_test.py`

Compares the performance of multiprocessing and multithreading for generating random numbers. 
- **Multiprocessing:** Uses multiple processes to execute `do_something` in parallel.
- **Multithreading:** Uses multiple threads for the same task.

### 5. **Process Creation**
**File:** `Process_Creation.py`

Demonstrates creating and managing multiple processes using Python's `multiprocessing` library. Two processes are created to compute the square and cube of a number.

### 6. **Semaphore Synchronization**
**File:** `Semaphore.py`

Shows how to use a semaphore to control access to a shared resource among threads. Each thread acquires the semaphore, performs a task, and then releases it.

### 7. **Serial and Parallel Programming**
**File:** `Serial and parallelprogramming.py`

Explains how to execute tasks in parallel using `ThreadPoolExecutor`. Two independent tasks are executed concurrently.

### 8. **Task Parallelism**
**File:** `Task_parallelism.py`

Demonstrates task parallelism by performing addition and subtraction operations concurrently using `ThreadPoolExecutor`. The execution time for both tasks is recorded.

### 9. **Threading Test**
**File:** `Threading_test.py`

Creates multiple threads to calculate the 30th Fibonacci number concurrently. This example highlights how threads can perform CPU-bound tasks.

