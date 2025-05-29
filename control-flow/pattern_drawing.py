#!/usr/bin/python3

size_patterns = int(input("Enter the size of the pattern: "))

i = 1
while i <= size_patterns:
    for j in range(0, size_patterns):
        print("*", end="")
        j = j + 1
    print()
    i = i + 1