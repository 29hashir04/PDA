# **Parallel and Distributed Programming **  

This repository provides an extensive collection of Python examples and scripts that delve into various aspects of parallel, distributed, and asynchronous programming. It serves as a practical guide to understanding core concepts such as multithreading, multiprocessing, message passing, and asynchronous programming with hands-on examples.  

---

## **Table of Contents**  
1. [Chapter 1: Parallel and Concurrent Programming](#chapter-1-parallel-and-concurrent-programming)  
2. [Chapter 2: Multithreading Examples in Python](#chapter-2-multithreading-examples-in-python)  
3. [Chapter 3: Multiprocessing Examples in Python](#chapter-3-multiprocessing-examples-in-python)  
4. [Chapter 4: Message Passing Interface (MPI)](#chapter-4-message-passing-interface-mpi)  
5. [Chapter 5: Asynchronous Programming](#chapter-5-asynchronous-programming)  

---

## **Chapter 1: Parallel and Distributed Programming**  
This chapter introduces the foundational concepts of parallel and concurrent programming and demonstrates their implementation using Python libraries.  

### **Topics Covered**  
- Data Parallelism  
- Task Parallelism  
- Serial and Parallel Programming  
- Process Creation and Synchronization  

### **Key Files**  
1. **`Data Parallelism.py`**: Implements efficient data parallel computation with NumPy.  
2. **`Do_something.py`**: Contains utility functions for multiprocessing and multithreading examples.  
3. **`Multiprocessing_test.py`**: Compares multiprocessing and multithreading performance.  
4. **`Semaphore.py`**: Demonstrates semaphore-based synchronization.  

---

## **Chapter 2: MultiThreading in Python**  
This chapter delves into multithreading, highlighting thread synchronization techniques, locking mechanisms, and basic thread operations.  

### **Topics Covered**  
- Thread Synchronization  
- Locking Mechanisms (`Lock`, `RLock`, `Semaphore`)  
- Thread Creation and Management  

### **Key Files**  
1. **`barrier.py`**: Synchronizes threads using the `Barrier` object.  
2. **`Condition.py`**: Implements producer-consumer synchronization with `Condition`.  
3. **`MyThreadClass_lock_2.py`**: Demonstrates safe thread operations with locks.  
4. **`Threading_with_queue.py`**: Showcases a producer-consumer pattern using `Queue`.  

---

## **Chapter 3: Multiprocessing in Python**  
Explore the power of multiprocessing in Python, including process creation, inter-process communication, and process pools.  

### **Topics Covered**  
- Process Synchronization  
- Inter-Process Communication (`Pipe`, `Queue`)  
- Daemon and Non-Daemon Processes  
- Custom Processes and Process Pools  

### **Key Files**  
1. **`communicating_with_pipe.py`**: Demonstrates communication using `Pipe`.  
2. **`naming_processes.py`**: Explains the importance of process naming.  
3. **`process_pool.py`**: Utilizes a pool of worker processes for parallel computation.  
4. **`run_background_processes.py`**: Highlights the difference between daemon and non-daemon processes.  

---

## **Chapter 4: Message Passing Interface (MPI)**  
This chapter provides examples of using the Message Passing Interface (MPI) for distributed computing and inter-process communication.  

### **Topics Covered**  
- Point-to-Point Communication  
- Collective Communication (`bcast`, `scatter`, `gather`)  
- Avoiding Deadlocks  

### **Key Files**  
1. **`Avoiding_Deadlock.py`**: Demonstrates deadlock-free point-to-point communication.  
2. **`Collective_Communication_using_Broadcast.py`**: Explains data broadcasting with `bcast`.  
3. **`Collective_Communication_Using_Scatter_function.py`**: Demonstrates data distribution using `scatter`.  
4. **`Point-to-Point Implementation.py`**: Implements direct communication between processes.  

---

## **Chapter 5: Asynchronous Programming**  
Learn about asynchronous programming in Python using `asyncio`, including task scheduling, coroutine management, and event-driven programming.  

### **Topics Covered**  
- `asyncio` Coroutines  
- Event Loops and Scheduling  
- ThreadPoolExecutor for Concurrent Task Execution  

### **Key Files**  
1. **`asyncio_coroutine.py`**: Simulates a finite state machine with coroutines.  
2. **`asyncio_event_looop.py`**: Implements event-driven task scheduling with `asyncio`.  
3. **`HeavyComputationSimulation.py`**: Compares sequential, thread pool, and process pool execution.  
4. **`ThreadPoolExecutor.py`**: Demonstrates task execution using `ThreadPoolExecutor`.  

