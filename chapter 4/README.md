# Chapter 4:
# Topics Covered:
## Message Passing Interface
---
## Files Overview

### 1. `Avoiding_Deadlock.py`
**Description**: Demonstrates point-to-point communication with proper send/receive calls to avoid deadlock.  
**Features**: 
- Process `0` sends an integer to process `4`.
- Process `1` sends a string to process `8`.
- Processes `4` and `8` receive and print the respective messages.  
![Avoiding_Deadlock](avoiding_deadlock.png)

### 2. `Collective_Communication_using_Broadcast.py`
**Description**: Illustrates collective communication using the `bcast` function.  
**Features**: 
- Process `0` shares a variable (`variable_to_share`) with all other processes.
- All processes print the shared variable after broadcasting.  
![Broadcast](broadcast.png)

### 3. `Collective_Communication_Using_gather_funcation.py`
**Description**: Shows the use of the `gather` function for collective communication.  
**Features**: 
- Each process computes its data as `(rank + 1)^2`.
- The root process (`rank 0`) gathers data from all processes and prints it.  
![Gather](gather.png)

### 4. `Collective_Communication_Using_Scatter_function.py`
**Description**: Demonstrates the `scatter` function for collective communication.  
**Features**: 
- Process `0` initializes an array and distributes its elements among all processes.
- Each process prints the element it received.  
![Scatter](scatter.png)

### 5. `Point-to-Point Implementation.py`
**Description**: Provides another example of point-to-point communication with distinct messages and processes.  
**Features**: 
- Process `0` sends an integer to process `4`.
- Process `1` sends a string to process `8`.
- Processes `4` and `8` receive and print the respective messages.  
![Point-to-Point](point_to_point.png)
