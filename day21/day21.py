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
# Given a monkey name and a node db, resolve the yell value.
#-------------------------------------------------------------------
def equal_yell(name, db):
    (status, value, lname, op, rname) = db[name]

    lvalue = resolve_yell(lname, db)
    rvalue = resolve_yell(rname, db)

    print("lvalue:", lvalue, "rvalue:", rvalue)

    return 4


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")

    day_input = get_input("day21_input.txt")
#    day_input = get_input("day21_example.txt")

    monkey_db = get_monkey_db(day_input)
    root_yell = resolve_yell('root', monkey_db)

    print("root will yell", root_yell)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")

#    day_input = get_input("day21_input.txt")
    day_input = get_input("day21_example.txt")

    monkey_db = get_monkey_db(day_input)
    human_yell = equal_yell('root', monkey_db)

    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2022, day 21")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
