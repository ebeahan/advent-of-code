#!/usr/bin/env python

from collections import Counter

file_path = "input"
column_a, column_b = [], []

try:
    with open(file_path, "r") as handler:
        for line in handler:
           split_line = line.split()
           column_a.append(int(split_line[0]))
           column_b.append(int(split_line[-1]))
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except IOError as e:
    print(f"An error occurred while handling this file: {e}")

count_dict = Counter(column_b)
result = 0
i = 0

for i in column_a:
    result += i  * count_dict.get(i, 0)
    i += 1

print(result)