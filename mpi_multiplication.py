# to execute the program using MPI, enter the following command in terminal in file's path:
# mpiexec -n 5 python mpi_multiplication.py

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    #get input matrices and perform multiplication using message passing
    print('Enter matrix 1 elements as follows: [[first, second], [third, fourth]]')
    first = int(input('first: '))
    second = int(input('second: '))
    third = int(input('third: '))
    fourth = int(input('fourth: '))
    matrix1 = [[first, second], [third, fourth]]
    print('Enter matrix 2 elements as follows: [[first, second], [third, fourth]]')
    first = int(input('first: '))
    second = int(input('second: '))
    third = int(input('third: '))
    fourth = int(input('fourth: '))
    matrix2 = [[first, second], [third, fourth]]
    print('matrix 1: \n', matrix1)
    print('matrix 2: \n', matrix2)

    # extract rows and columns
    row1 = matrix1[0]
    row2 = matrix1[1]
    column1 = [matrix2[i][0] for i in range(2)]
    column2 = [matrix2[i][1] for i in range(2)]

    # send rows and columns to other processes using message passing
    comm.send(row1, dest=1)
    comm.send(column1, dest=1)
    comm.send(row1, dest=2)
    comm.send(column2, dest=2)
    comm.send(row2, dest=3)
    comm.send(column1, dest=3)
    comm.send(row2, dest=4)
    comm.send(column2, dest=4)

    # receive each element from other processes
    element11 = comm.recv(source=1)
    element12 = comm.recv(source=2)
    element21 = comm.recv(source=3)
    element22 = comm.recv(source=4)

    # print the result
    multiplied = [[element11, element12],
                  [element21, element22]]
    print('multiplication output: \n', multiplied)

if rank != 0:
    # receive assigned row and column and return the sum of multiplication to rank 0 using message passing
    row = comm.recv(source=0)
    column = comm.recv(source=0)
    element = sum([row[i] * column[i] for i in range(2)])
    comm.send(element, dest=0)

