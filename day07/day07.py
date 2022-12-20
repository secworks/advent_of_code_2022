#!/usr/bin/env python3
#=======================================================================
#
# day07.py
# --------
# Solutions to Advent of Code 2022, day 07.
#
# (c) 2022 Joachim Strömbergson
# SPDX-License-Identifier: MIT
#
#=======================================================================

# Imports as needed.


# DirNode is a directory in the file system structure. It can keep
# track of files and subdirs. It has a name and a total size of
# all files in the dir as well as all subdirs.
class DirNode:
    def __init__(self):
        self.name = ""
        self.parent = None
        self.total_weight = 0
        self.subdirs = []
        self.files = []


# FileNode is a file in the file system structure. It has a name
# and a size.
class FileNode:
    def __init__(self):
        self.name = ""
        self.size = 0


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            l.append(line.strip())
    return l


def parse_commands(cmds):
    for cmd in cmds:
        if '$' in cmd:
            print(cmd, "is a command")
        elif 'dir'in cmd:
            (d, n) = cmd.split(" ")
            print(n, "is a directory")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")

#    my_input = get_input("day07_input.txt")
    my_input = get_input("day07_example.txt")

    my_tree = []
    my_tree.append(FileNode())
    parse_commands(my_input)
    print(my_tree)
    print(my_input)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2022, day 07")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
