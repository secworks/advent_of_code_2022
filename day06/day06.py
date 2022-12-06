#!/usr/bin/env python3
#=======================================================================
#
# day06.py
# --------
# Solutions to Advent of Code 2022, day 06.
#
# (c) 2022 Joachim Strömbergson
# SPDX-License-Identifier: MIT
#
#=======================================================================

# Imports as needed.


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            l.append(line.strip())
    return l


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def find_unique_chars(s):
    unique = True

    for i in range(len(s)):
        if i == 0:
            if s[i] in s[1:]:
                unique = False
        elif i == len(s):
            if s[i] in s[:i]:
                unique = False
        else:
            if (s[i] in s[:i]) or (s[i] in s[(i + 1):]):
                unique = False
    return unique


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")
    my_input = get_input("day06_input.txt")[0]

    done = False
    for i in range(len(my_input) - 4):
        if not done and find_unique_chars(my_input[i : (i + 4)]):
            print("marker at:", i + 4)
            done = True
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")

    my_input = get_input("day06_input.txt")[0]

    done = False
    for i in range(len(my_input) - 14):
        if not done and find_unique_chars(my_input[i : (i + 14)]):
            print("marker at:", i + 14)
            done = True
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2022, day 06")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
