#!/usr/bin/env python3
#=======================================================================
#
# day05.py
# --------
# Solutions to Advent of Code 2022, day 05.
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
# Build the list of stacks
#-------------------------------------------------------------------
def get_initial_stacks(is_example):
    if is_example:
        stacks = [['Z','N'],\
                  ['M','C','D'],\
                  ['P']]
    else:
        stacks = [['J','F','C','N','D','B','W'],
                  ['T','S','L','Q','V','Z','P'],
                  ['T','J','G','B','Z','P'],
                  ['C','H','B','Z','J','L','T','D'],
                  ['S','J','B','V','G'],
                  ['Q','S','P'],
                  ['N','P','M','L','F','D','V','B'],
                  ['R','L','D','B','F','M','S','P'],
                  ['R','T','D','V'],
                  ]

        # Flip the order to to work with append()
        for i in range(len(stacks)):
            stacks[i].reverse()

    return stacks


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_commands(cmdlist):
    cmds = []
    for l in cmdlist:
        (f1, f2, f3, f4, f5, f6) = l.split(" ")
        cmds.append((f2, f4, f6))
    return cmds


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def exe_command(stacks, cmd):
    (n, f, t) = cmd
    number = int(n)
    from_stack = int(f) - 1
    to_stack = int(t) - 1

    for n in range((number)):
        crate = stacks[from_stack].pop()
        stacks[to_stack].append(crate)
#        print("moving crate", crate, "from stack", \
#              from_stack, "to stack", to_stack)
    return stacks


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def move_crates(stacks, commands):
    for cmd in commands:
        stacks = exe_command(stacks, cmd)
    return stacks


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def exe_command_9001(stacks, cmd):
    (n, f, t) = cmd
    number = int(n)
    from_stack = int(f) - 1
    to_stack = int(t) - 1

    tmp_stack = []
    for n in range((number)):
        tmp_stack.append(stacks[from_stack].pop())
    tmp_stack.reverse()
    stacks[to_stack] += tmp_stack
    return stacks


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def move_crates_9001(stacks, commands):
    for cmd in commands:
        stacks = exe_command_9001(stacks, cmd)
    return stacks


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_top_crates(stacks):
    top = ""
    for stack in stacks:
        top += stack.pop()
    return top


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")
    my_input = get_input("day05_input.txt")
#    my_input = get_input("day05_example.txt")
    my_stacks = get_initial_stacks(False)
    my_commands = get_commands(my_input)
    my_stacks = move_crates(my_stacks, my_commands)
    my_top_crates = get_top_crates(my_stacks)
    print("top crates:", my_top_crates)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")
    my_input = get_input("day05_input.txt")
#    my_input = get_input("day05_example.txt")
    my_stacks = get_initial_stacks(False)
    my_commands = get_commands(my_input)
    my_stacks = move_crates_9001(my_stacks, my_commands)
    my_top_crates = get_top_crates(my_stacks)
    print("top crates:", my_top_crates)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2022, day 05")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
