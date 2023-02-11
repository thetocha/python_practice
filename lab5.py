def file_processing(input_file, output_file_1, output_file_2):
    with open(input_file, 'r') as input_f:
        data = input_f.readlines()

    raise_flag = True
    decline_flag = True
    for string in data:
        string = string.rstrip('\n')
        for i in range(len(string) - 1):
            if string[i] > string[i + 1]:
                raise_flag = False
            elif string[i] < string[i + 1]:
                decline_flag = False
        if raise_flag:
            with open(output_file_1, 'a') as output_f_1:
                output_f_1.write(string + '\n')
        if decline_flag:
            with open(output_file_2, 'a') as output_f_2:
                output_f_2.write(string + '\n')
        raise_flag = True
        decline_flag = True


if __name__ == '__main__':
    file_processing("input.txt", "raise.txt", "decline.txt")
