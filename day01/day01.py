#!/usr/bin/env python3
#=======================================================================
#
# day01.py
# --------
# Solutions to Advent of Code 2022, day 01.
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
def get_elflists(indata):
    # Build list of lists with all items each elf has.
    elves = []
    elf_items = []

    for i in indata:
        if i == '':
            elves.append(elf_items)
            elf_items = []

        else:
            elf_items.append(int(i))
    # Add items for final elf.
    elves.append(elf_items)

    return elves


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")
    my_input = get_input("day01_input.txt")
#    my_input = get_input("day01_testdata.txt")
    my_elves = get_elflists(my_input)

    elf_id = 0
    max_elf = 0
    max_calories = 0

    for elf in my_elves:
        elf_id += 1
        calories = 0
        for i in elf:
            calories += i
        if calories > max_calories:
            max_elf = elf_id
            max_calories = calories

    print("Max calories:", max_calories, "for elf", max_elf)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def update_fatness(elves, elf, elf_id):
    c = sum(elf)

    (eid0, c0) = elves[0]
    (eid1, c1) = elves[1]
    (eid2, c2) = elves[2]

    if c > c0:
        elves[2] = elves[1]
        elves[1] = elves[0]
        elves[0] = (elf_id, c)

    elif c > c1:
        elves[2] = elves[1]
        elves[1] = (elf_id, c)

    elif c > c2:
        elves[2] = (elf_id, c)

    return elves

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")

    my_input = get_input("day01_input.txt")
#    my_input = get_input("day01_testdata.txt")
    my_elves = get_elflists(my_input)

    elf_id = 0
    fattest_elves = [(0,0), (0,0), (0,0)]
    # Get the three fattest elves
    for elf in my_elves:
        elf_id += 1
        fattest_elves = update_fatness(fattest_elves, elf, elf_id)
    print("Fattest elves:", fattest_elves)

    # Calculate total sum of all calories
    csum = 0
    for elf in fattest_elves:
        (eid, c) = elf
        csum += c
    print("Total calories:", csum)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2022, day 01")
print("==========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
