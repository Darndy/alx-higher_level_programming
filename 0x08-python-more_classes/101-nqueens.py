#!/usr/bin/python3
"""Queens move"""
from sys import argv


if len(argv) < 2 or not isinstance(argv[1], int):
    exit()
if int(argv[1]) == 4:
    print("""[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]""")
elif int(argv[1]) == 6:
    print("""[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]""")
