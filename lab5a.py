#!/usr/bin/env python3
# Author ID: adonkor

def read_file_string(file_name):
    f = open(file_name, 'r')
    content = f.read()
    f.close()
    return content

def read_file_list(file_name):
    f = open(file_name, 'r')
    lines = [line.strip() for line in f]
    f.close()
    return lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
