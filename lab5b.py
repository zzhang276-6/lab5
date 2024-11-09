#!/usr/bin/env python3
# Author ID: zzhang276

def read_file_string(file_name):
    # f = open(file_name, 'r')
    # string = f.read()
    # f.close()
    # return string
    with open(file_name, 'r') as f:
        return f.read()
def read_file_list(file_name):
    # f = open(file_name, 'r')
    # list = f.read().splitlines()
    # f.close()
    # return list
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]
def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    with open(file_name, 'a') as f:
        return f.write(string_of_lines)
def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')
def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    with open(file_name_read, 'r') as f:
        firstfile = f.readlines()
    with open(file_name_write, 'w') as f1:
        count = 1
        for item in firstfile:
            f1.write(f'{count}:{item}')
            count += 1
if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))