# Scheduling Algorithms Simulator

This project provides a hands-on simulation of four fundamental scheduling algorithms used in operating systems:
- **FCFS (First-Come, First-Served)**
- **SJF (Shortest Job First)**
- **SRTN (Shortest Remaining Time Next)**
- **Round Robin** (with a customizable time quantum)

## Project Goals

Developed as part of my Operating Systems course, this simulator aims to:
- Illustrate the inner workings of each scheduling algorithm
- Calculate and compare key performance metrics:
  - Waiting time (per process and average)
  - Turnaround time (per process and average)
- Analyze the impact of context switching on algorithm efficiency
- Provide a flexible tool for experimenting with different scheduling scenarios

## Getting Started

1. **Prerequisites:** Ensure you have Python installed on your system.
2. **Clone or download this repository.**
3. **Run the simulation:** Execute the `main.py` file from your terminal.

## Sample Data and Output

The simulator comes preloaded with sample process data for testing:

| Process | Arrival Time (ms) | CPU Burst Time (ms) |
|---------|-------------------|---------------------|
| P1      | 0                 | 6                   |
| P2      | 3                 | 2                   |
| P3      | 5                 | 1                   |
| P4      | 9                 | 7                   |
| P5      | 10                | 4                   |
| P6      | 11                | 3                   |

The output will display detailed results for each algorithm, including:
- A table showing the arrival time, burst time, completion time, turnaround time, and waiting time for each process.
- Average turnaround time and average waiting time for all processes.
- A comparison of algorithm performance with and without context switching (0.4 ms).

## Customization and Exploration

- **Modify the sample data:** Experiment with different process arrival times and burst times in `main.py`.
- **Adjust the time quantum:** Change the Round Robin quantum value in `main.py` to observe its impact.
- **Implement new algorithms:** Extend the simulator by adding your own scheduling algorithms!

## Code Structure and Implementation

The core of the project lies in two Python classes:
- **SchedulingRow:** Represents a single process, storing its attributes and providing a method to print its information.
- **SchedulingAlgorithm:** Contains the logic for each scheduling algorithm (`compute` and `compute2` methods) and methods to add processes, calculate metrics, and print results.

Feel free to explore the code to gain a deeper understanding of the implementation.

## Key Features

- **Clear and well-commented code:** Easy to read and understand.
- **Modular design:** Promotes code reusability and extensibility.
- **Context switching simulation:** Provides insights into real-world scheduling scenarios.
- **Customization options:** Allows for experimentation and learning.

## Let's Connect!

If you have any questions, feedback, or ideas for collaboration, don't hesitate to reach out. You can find my contact information in my GitHub profile. Let's continue exploring the fascinating world of operating systems and scheduling algorithms together!
