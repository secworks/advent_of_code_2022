#!/usr/bin/env python3
#=======================================================================
#
# day02.py
# --------
# Solutions to Advent of Code 2022, day 02.
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
def get_rulebook(filename):
    my_input = get_input(filename)
    book = []

    for line in my_input:
        l, r = line.split(" ")

        if l == "A":
            his_rule = "rock"
        elif l == "B":
            his_rule = "paper"
        else:
            his_rule = "scissors"

        if r == "X":
            my_rule = "rock"
        elif r == "Y":
            my_rule = "paper"
        else:
            my_rule = "scissors"

        book.append((his_rule, my_rule))

    return book


#-------------------------------------------------------------------
# Reinterpret the rules differently.
#-------------------------------------------------------------------
def get_other_rulebook(filename):
    my_input = get_input(filename)
    book = []

    for line in my_input:
        l, r = line.split(" ")

        if r == "X":
            # Loose the game
            if l == "A":
                his_rule = "rock"
                my_rule = "scissors"
            elif l == "B":
                his_rule = "paper"
                my_rule = "rock"
            else:
                his_rule = "scissors"
                my_rule = "paper"

        elif r == "Y":
            # Draw the game
            if l == "A":
                his_rule = "rock"
                my_rule = "rock"
            elif l == "B":
                his_rule = "paper"
                my_rule = "paper"
            else:
                his_rule = "scissors"
                my_rule = "scissors"

        else:
            # Win the game
            if l == "A":
                his_rule = "rock"
                my_rule = "paper"
            elif l == "B":
                his_rule = "paper"
                my_rule = "scissors"
            else:
                his_rule = "scissors"
                my_rule = "rock"

        book.append((his_rule, my_rule))

    return book


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def play_game(book):
    result = []

    s = 0
    for rule in book:
        (his_move, my_move) = rule

        if my_move == "rock":
            shape_score = 1
        elif my_move == "paper":
            shape_score = 2
        else:
            shape_score = 3

        if ((my_move == "rock") and (his_move == "scissors")):
            outcome = 6
        elif ((my_move == "paper") and (his_move == "rock")):
            outcome = 6
        elif ((my_move == "scissors") and (his_move == "paper")):
            outcome = 6
        elif my_move == his_move:
            outcome = 3
        else:
            outcome = 0

        s += shape_score + outcome
    return s


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")
#    my_rulebook = get_rulebook("day02_example.txt")
    my_rulebook = get_rulebook("day02_input.txt")
    my_result = play_game(my_rulebook)
    print("my result", my_result)
    print("")

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")
#    my_rulebook = get_other_rulebook("day02_example.txt")
    my_rulebook = get_other_rulebook("day02_input.txt")
    my_result = play_game(my_rulebook)
    print("my result", my_result)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2022, day 02")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
