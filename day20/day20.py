#!/Usr/bin/env python3
#=======================================================================
#
# day20.py
# --------
# Solutions to Advent of Code 2022, day 20.
#
# (c) 2022 Joachim Strömbergson
# SPDX-License-Identifier: MIT
#
#=======================================================================

# Imports as needed.

#-------------------------------------------------------------------
# CPU is a model of the constrained cpu.
#-------------------------------------------------------------------
class CPU:
    def __init__(self, filename):
        self.state = 'START'
        self.x = 1
        self.dx = 0
        self.cycle = 1
        self.instr = ""
        self.pc = 0
        self.finished = False

        self.program = []
        with open(filename,'r') as f:
            for line in f:
                self.program.append(line.strip())


    def update(self):
        if self.state == 'START':
            if self.pc == len(self.program):
                self.finished = True
            else:
                self.instr = self.program[self.pc]
                self.pc += 1

#                print("Cycle", self.cycle, "Starting instruction", self.instr, " x =", self.x)

                if 'noop' in self.instr:
                    self.dx = 0
                    self.state = 'COMPLETE'

                else:
                    self.dx = int(self.instr.split(' ')[1])
                    self.state = 'EXECUTE'


        elif self.state == 'EXECUTE':
#            print("Cycle", self.cycle, "Executing instruction", self.instr, " x =", self.x)
            self.state = 'COMPLETE'
            self.cycle += 1


        elif self.state == 'COMPLETE':
#            print("Cycle", self.cycle, "Completing instruction", self.instr, " x =", self.x)
            self.state = 'START'
            self.x += self.dx
            self.cycle += 1


    def get_cycle(self):
        return self.cycle


    def get_x(self):
        return self.x


    def get_strength(self):
        return self.cycle * self.x


    def done(self):
        return self.finished


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")

    my_input = get_input("day20_input.txt")
    my_input = get_input("day20_example.txt")

    print(my_input)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2022, day 20")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
