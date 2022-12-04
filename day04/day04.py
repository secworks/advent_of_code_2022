#!/usr/bin/env python3
#=======================================================================
#
# day04.py
# --------
# Solutions to Advent of Code 2022, day 04.
#
#=======================================================================


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
def get_ranges(indata):
    rl = []
    for i in indata:
        first, last = i.split(',')
        firstmin, firstmax = first.split('-')
        lastmin, lastmax = last.split('-')
        rl.append((int(firstmin), int(firstmax),
                   int(lastmin), int(lastmax)))
    return rl


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_num_fully_overlapped(rl):
    foc = 0
    for r in rl:
        (fmin, fmax, lmin, lmax) = r
        if (fmin >= lmin and fmax <= lmax) or \
           (lmin >= fmin and lmax <= fmax):
           foc += 1
    return foc


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_num_overlapped(rl):
    poc = 0
    for r in rl:
        (fmin, fmax, lmin, lmax) = r
        if (fmin >= lmin and fmax <= lmax) or \
           (lmin >= fmin and lmax <= fmax) or \
           (fmin >= lmin and fmin <= lmax) or \
           (lmin >= fmin and lmin <= fmax):
           poc += 1
    return poc


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")
    my_input = get_input("day04_input.txt")
#    my_input = get_input("day04_example.txt")

    my_ranges = get_ranges(my_input)
    overlapped = get_num_fully_overlapped(my_ranges)
    print("Number of fully overlapped ranges:", overlapped)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")

    my_input = get_input("day04_input.txt")
#    my_input = get_input("day04_example.txt")

    my_ranges = get_ranges(my_input)
    overlapped = get_num_overlapped(my_ranges)
    print("Number of overlapping ranges:", overlapped)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2022, day 04")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
