from random import random


def max_el(matrix):
    max_value = 0
    index = 0
    for i, elem in enumerate(matrix):
        if elem >= max_value:
            max_value = elem
            index = i
    return index


def sum_mtr(matrix):
    first_index = 0
    first_flag = False
    last_index = 0
    summ = 0
    for i in range(len(matrix)):
        if matrix[i] < 0:
            if not first_flag:
                first_index = i
                first_flag = True
            elif first_flag:
                last_index = i

    for i in matrix[first_index + 1:last_index]:
        summ += i

    return summ


def reorganisation(matrix, x):
    index = 0
    lower = []
    greater = []
    for i, elem in enumerate(matrix):
        if abs(elem) < abs(x):
            lower.append(elem)
        else:
            greater.append(elem)
    matrix = lower + greater
    return matrix


def create_matrix(size):
    matrix = [0 for i in range(size)]
    for i in range(size):
            matrix[i] = round(random() * 100 % 11)
    return matrix


if __name__ == '__main__':
    print(matrix := create_matrix(3))
    print(max_el(matrix))
    print(sum_mtr(matrix))
    print(reorganisation(matrix, 6))
