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

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
