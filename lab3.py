from random import random


def create_matrix(size):
    matrix = [[0 for i in range(size)] for i in range(2 * size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = round(random() * 100 % 11)
            matrix[i + size][j] = matrix[i][j]
    return matrix


def not_zero_columns(matrix, size):
    not_null = True
    count = 0
    for i in range(size):
        for j in range(size):
            if matrix[j][i] == 0:
                not_null = False
        if not_null:
            count += 1
            not_null = True
    return count


def raise_sequence(matrix, size):
    raise_flag = True
    for i in range(size):
        for j in range(size - 1):
            if matrix[i][j] >= matrix[i][j + 1]:
                raise_flag = False
        if raise_flag:
            return i
    return -1


if __name__ == "__main__":
    print(m_matrix := create_matrix(m_size := 3))
    print(not_zero_columns(m_matrix, m_size))
    print(raise_sequence(m_matrix, m_size))
