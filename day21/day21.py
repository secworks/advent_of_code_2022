#!/Usr/bin/env python3
#=======================================================================
#
# day21.py
# --------
# Solutions to Advent of Code 2022, day 21.
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
def get_monkey_db(l):
    monkey_db = {}

    for n in l:
        if len(n.split(' ')) == 2:
            (name, value) = n.split(' ')
            monkey_db[name[:-1]] = ('resolved', value, None, None, None)
        else:
            (name, lname, op, rname) = n.split(' ')
            monkey_db[name[:-1]] = ('unresolved', None, lname, op, rname)
    return monkey_db


#-------------------------------------------------------------------
# Given a monkey name and a node db, resolve the yell value.
#-------------------------------------------------------------------
def resolve_yell(name, db):
    (status, value, lname, op, rname) = db[name]

    if status == 'resolved':
        return int(value)

    else:
        lvalue = resolve_yell(lname, db)
        rvalue = resolve_yell(rname, db)

        if op == '+':
            return lvalue + rvalue

        elif op == '-':
            return lvalue - rvalue

        elif op == '*':
            return lvalue * rvalue

        elif op == '/':
            return int(lvalue / rvalue)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")

    my_input = get_input("day21_input.txt")
#    my_input = get_input("day21_example.txt")

    my_monkey_db = get_monkey_db(my_input)
    print(my_monkey_db)
    my_yell = resolve_yell('root', my_monkey_db)

    print("root will yell", my_yell)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2022, day 21")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
