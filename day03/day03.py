#!/usr/bin/env python3
#=======================================================================
#
# day03.py
# --------
# Solutions to Advent of Code 2022, day 03.
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
def get_rucksacks(contents):
    rucksacks = []
    for c in contents:
        first = c[0 : len(c)//2]
        second = c[len(c)//2 :]
        rucksacks.append((first, second))
    return rucksacks


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_duplicate_types(rucksack):
    dup = []
    (l, r) = rucksack
    for c in l:
        if (c in r) and (c not in dup):
            dup.append(c)
    return dup


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_duplicates(rucksacks):
    duplicates = []
    for rucksack in rucksacks:
        duplicates.append(get_duplicate_types(rucksack))
    return duplicates


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_priorities(items):
    priolist = []
    for item in items:
        for j in item:
            if j.isupper():
                priolist.append(ord(j) - 38)
            else:
                priolist.append(ord(j) - 96)
    return priolist


#-------------------------------------------------------------------
# Divide input list into list of lists with three strings each
#-------------------------------------------------------------------
def get_3rucksacks(sacks):
    l3 = []
    for i in range(0, len(sacks), 3):
        tmp = [sacks[i], sacks[i + 1], sacks[i + 2]]
        l3.append(tmp)
    return l3


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_common_chars(sacks):
    return set.intersection(*map(set,sacks))


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")
    my_input = get_input("day03_input.txt")
#    my_input = get_input("day03_example.txt")
    my_rucksacks = get_rucksacks(my_input)
    my_duplicates = get_duplicates(my_rucksacks)
    my_priorities = get_priorities(my_duplicates)

    print("my priorities", sum(my_priorities))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")

    my_input = get_input("day03_input.txt")
#    my_input = get_input("day03_example.txt")
    my_3rucksacks = get_3rucksacks(my_input)

    my_duplicates = []
    for sacks in my_3rucksacks:
        my_duplicates.append(get_common_chars(sacks))

    my_priorities = get_priorities(my_duplicates)
    print("my priorities", sum(my_priorities))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2022, day 03")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
