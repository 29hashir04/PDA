# Chapter 2:
# Topics Covered:
## Multi-Threading 

This repository contains multiple examples of Python multi-threading, synchronization mechanisms, and concurrent programming. Below is an explanation of each file included in the codebase:

## **1. barrier.py**

This script demonstrates the use of the `Barrier` synchronization object. 

### Functionality:
- Three runners (`Huey`, `Dewey`, `Louie`) race and wait at the barrier.
- The race starts concurrently, and all threads must reach the barrier before proceeding further.

### Key Components:
- `Barrier` ensures threads synchronize at a specific point.
- `Thread` class used to run each runner in parallel.

---

## **2. Condition.py**

This script illustrates the use of a `Condition` object for thread synchronization.

### Functionality:
- A `Producer` thread produces items up to a limit (10 items).
- A `Consumer` thread consumes items, waiting when none are available.

### Key Components:
- `Condition` used to manage producer-consumer synchronization.
- `notify` and `wait` methods used for inter-thread communication.

---

## **3. Event.py**

This script demonstrates the use of `Event` for signaling between threads.

### Functionality:
- A `Producer` thread adds random items to a shared list.
- A `Consumer` thread pops items when signaled by the producer.

### Key Components:
- `Event` is used to set, clear, and wait for events.

---

## **4. MyThreadClass_lock_2.py**

This script uses a `Lock` object to ensure thread-safe operations.

### Functionality:
- Nine threads perform tasks with varying durations.
- Each thread acquires a lock before printing information to avoid overlapping output.

### Key Components:
- `Lock` used for mutual exclusion.
- Threads created using a custom `MyThreadClass`.

---

## **5. MyThreadClass_lock.py**

This script is a simpler version of `MyThreadClass_lock_2.py`, also demonstrating the use of a `Lock` object.

### Functionality:
- Nine threads perform tasks and acquire a lock to ensure thread-safe operations.

### Key Components:
- `Lock` ensures proper synchronization of shared resources.

---

## **6. MyThreadClass.py**

This script demonstrates basic thread creation and execution without synchronization.

### Functionality:
- Threads execute and print their process IDs.

### Key Components:
- Simple `Thread` implementation.

---

## **7. Rlock.py**

This script demonstrates the use of `RLock` (reentrant lock) for thread-safe recursive operations.

### Functionality:
- Adds and removes items in a shared `Box` using threads.
- `RLock` allows a thread to acquire the same lock multiple times.

### Key Components:
- `RLock` ensures safe recursive locking.

---

## **8. Semaphore.py**

This script demonstrates the use of a `Semaphore` for controlling thread access.

### Functionality:
- A producer thread generates items.
- A consumer thread waits for items to be produced.

### Key Components:
- `Semaphore` controls access to shared resources.

---

## **9. Thread_definition.py**

This script shows basic thread creation using the `Thread` class.

### Functionality:
- Ten threads call a function and print their thread numbers.

### Key Components:
- Simple demonstration of thread initialization and execution.

---

## **10. Thread_determine.py**

This script demonstrates naming and managing threads.

### Functionality:
- Three threads execute different functions.
- Prints thread names and completion statuses.

### Key Components:
- Thread naming and execution flow control.

---

## **11. Thread_name_and_processes.py**

This script demonstrates thread creation and process management.

### Functionality:
- Threads print their process IDs.

### Key Components:
- Demonstrates threads' relationship with the parent process.

---

## **12. Threading_with_queue.py**

This script illustrates thread synchronization using a `Queue`.

### Functionality:
- A producer thread adds items to a queue.
- Multiple consumer threads remove items from the queue.

### Key Components:
- `Queue` ensures thread-safe data exchange.
- Producer-consumer pattern implemented with multiple consumers.
