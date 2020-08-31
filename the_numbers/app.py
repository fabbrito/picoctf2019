#!/usr/bin/env python3

v1 = [16, 9, 3, 15, 3, 20, 6]
v2 = [20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]

flag = ''.join([chr(x+ord('a')-1) for x in v1]) + \
    '{' + ''.join([chr(x+ord('a')-1) for x in v2]) + '}'

print(flag)
