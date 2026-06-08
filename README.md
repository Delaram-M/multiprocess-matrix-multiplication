# Multi-process Matrix Multiplication

This program gets two 2*2 matrices as input, multiplies them using multiple processors, and outputs the result.
This program uses mpi4py, which provides Message Passing Interface (MPI) bindings for Python.

# Instructions
You first need to install MPI and mpi4py.

To execute the program:
1. Open a terminal.
2. Navigate to the directory of the script.
3. Execute the command: ``` mpiexec -n 5 python mpi_multiplication.py ```.

This will run the program with 5 processors.
