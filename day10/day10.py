#!/usr/bin/env python3
#=======================================================================
#
# day10.py
# --------
# Solutions to Advent of Code 2022, day 10.
#
# (c) 2022 Joachim Strömbergson
# SPDX-License-Identifier: MIT
#
#=======================================================================

# Imports as needed.


#-------------------------------------------------------------------
# CPU is model of the constrained cpu.
#-------------------------------------------------------------------
class CPU:
    def __init__(self, program):
        self.state = 'INIT'
        self.x = 1
        self.cycles = 1
        self.icycles = 0
        self.pc = 0
        self.program = program


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
def cpu_get_strength(cpu):
    return cpu.cycles * cpu.x


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def cpu_step(cpu):
    pass


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def cpu_done(cpu):
    return cpu.state == 'DONE'


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")

    my_program = get_input("day10_input.txt")
    my_program = get_input("day10_short_example.txt")
    print(my_program)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")

    my_program = get_input("day10_input.txt")
    my_program = get_input("day10_short_example.txt")
    print(my_program)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2022, day 10")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================