# Chapter 3:
# Topics Covered:
## Multiprocessing Examples in Python

---

### 1. Communicating with Pipes

**File**: `communicating_with_pipe.py`  
**Description**: Demonstrates inter-process communication using `Pipe`. One process creates items (integers from 0 to 9) and another process processes these items by squaring them.  
**Key Functions**:
- `create_items(pipe)`: Sends numbers to the pipe.
- `multiply_items(pipe_1, pipe_2)`: Squares the numbers received from one pipe and sends them to another.

---

### 2. Communicating with Queues

**File**: `communicating_with_queue.py`  
**Description**: Illustrates the use of `Queue` for producer-consumer communication. A producer process generates random integers and adds them to the queue, while a consumer process retrieves and processes these integers.  
**Key Classes**:
- `producer(queue)`: Produces random integers and appends them to the queue.
- `consumer(queue)`: Consumes integers from the queue and processes them.

---

### 3. Daemon and Non-Daemon Processes

**File**: `derom.py`  
**Description**: Explains the difference between daemon and non-daemon processes. Daemon processes run in the background and are terminated when the main program exits.  
**Key Features**:
- Demonstrates separate behavior for daemon and non-daemon processes.

---

### 4. Killing Processes

**File**: `killing_processes.py`  
**Description**: Shows how to terminate a process forcefully. The script creates a process that counts numbers and demonstrates starting, terminating, and joining a process.  
**Key Functions**:
- `foo()`: Prints numbers with a delay to simulate work.

---

### 5. Custom Functions

**File**: `myFunc.py`  
**Description**: A simple example of passing arguments to a function executed by a process.  
**Key Function**:
- `myFunc(i)`: Outputs numbers up to the given argument.

---

### 6. Naming Processes

**File**: `naming_processes.py`  
**Description**: Demonstrates how to name processes explicitly. This helps in debugging and identifying processes in logs.  
**Key Features**:
- Names processes explicitly or uses the default names.

---

### 7. Subclassing Processes

**File**: `process_in_subclass.py`  
**Description**: Explores how to create custom processes by subclassing the `Process` class.  
**Key Class**:
- `MyProcess`: A custom process class with a `run` method.

---

### 8. Process Pools

**File**: `process_pool.py`  
**Description**: Utilizes a `Pool` of worker processes to parallelize computation. The script calculates the square of numbers from 0 to 99.  
**Key Features**:
- `Pool.map()`: Maps the function to the input list and distributes the workload among processes.

---

### 9. `processes_barrier.py`
This script demonstrates the use of a `Barrier` to synchronize processes and a `Lock` for serialized printing.

- **Key Features**:
  - `Barrier`: Ensures that multiple processes reach a certain point before any of them continues execution.
  - `Lock`: Ensures that print statements from multiple processes do not interfere with each other.

- **Functions**:
  - `test_with_barrier(synchronizer, serializer)`: Processes synchronize on a `Barrier` before printing.
  - `test_without_barrier()`: Processes print without synchronization.

### 10. `run_background_processes.py`
Illustrates the difference between daemon and non-daemon processes.

- **Key Features**:
  - Daemon processes terminate when the main program exits.
  - Non-daemon processes continue to run even after the main program ends.

- **Execution**:
  - `background_process`: Set as a daemon.
  - `NO_background_process`: Set as a non-daemon.

### 11. `run_background_processes_no_daemons.py`
Similar to `run_background_processes.py`, but both processes (`background_process` and `NO_background_process`) are non-daemon.

- **Purpose**:
  - Demonstrates how the termination behavior changes when no process is marked as a daemon.

### 12. `spawning_processes.py`
Shows how to spawn multiple processes and execute a function with arguments.

- **Key Features**:
  - Spawns processes to execute `myFunc` with a unique argument.
  - Uses `join` to ensure processes complete before the script exits.

- **Function**:
  - `myFunc(i)`: Prints the process number and loops based on the input.

### 13. `spawning_processes_namespace.py`
Expands on `spawning_processes.py` by organizing the function (`myFunc`) in a separate file/module.

- **Structure**:
  - Imports `myFunc` from another module.
  - Demonstrates modularity and code reuse in multiprocessing scripts.

