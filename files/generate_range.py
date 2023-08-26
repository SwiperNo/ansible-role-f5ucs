#!/usr/bin/env python

import sys

def generate_range(start, end, step):
    current = start
    while current < end:
        yield current
        current += step

if __name__ == '__main__':
    start, end, step = map(int, sys.argv[1:])
    print(" ".join(map(str, generate_range(start, end, step))))
