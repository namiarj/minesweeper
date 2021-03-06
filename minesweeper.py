#!/usr/bin/python3

import random
import os

class minePixel:
    isMine = False
    isFlag = False
    isSweeped = False
    minesAround = 0

x = 12 
y = 12
mines = 30

matrix = [[minePixel() for i in range(x)] for j in range(y)]

# putting mines randomly in pixels
counter = 0
while counter < mines:
    rand_x = random.randint(0, x-1)
    rand_y = random.randint(0, y-1)
    if matrix[rand_x][rand_y].isMine == False:
        matrix[rand_x][rand_y].isMine = True
        counter += 1

# get number of the mines around the point
def getMinesAround(x_, y_):
    counter = 0
    range = [-1, 0, +1]
    for i in range:
        for j in range:
            x_tmp = x_ + i
            y_tmp = y_ + j
            if not (y_tmp >= y or x_tmp >= x or y_tmp < 0 or x_tmp < 0):
                if matrix[x_tmp][y_tmp].isMine:
                    counter += 1
    return counter

def strBoldRed(str):
    return "\x1b[1;31m" + str + "\x1b[0m"

def strYellow(str):
    return "\x1b[33m" + str + "\x1b[0m"

def printMatrix():
    os.system("clear")
    # x axis
    print("\n  ", end="")
    for j in range(x):
        if j >= 10:
            print(strBoldRed(chr(j + 55) + " "), end="")
        else:
            print(strBoldRed(str(j) + " "), end="")
    print("x")

    for i in range(y):
        if i >= 10:
            print(strBoldRed(chr(i + 55) + " "), end="")
        else:
            print(strBoldRed(str(i) + " "), end="")
        for j in range(x):
            if matrix[j][i].isSweeped:
                print(str(matrix[j][i].minesAround) + " ", end="")
            elif matrix[j][i].isFlag:
                print(strYellow("? "), end="")
            else:
                print("- ", end="")
        print()
    print("y")
    print()

def printGameoverMatrix(x_, y_):
    os.system("clear")
    print(strBoldRed("\nGame Over!"))
    # x axis
    print("\n  ", end="")
    for j in range(x):
        if j >= 10:
            print(strBoldRed(chr(j + 55) + " "), end="")
        else:
            print(strBoldRed(str(j) + " "), end="")
    print("x")

    for i in range(y):
        if i >= 10:
            print(strBoldRed(chr(i + 55) + " "), end="")
        else:
            print(strBoldRed(str(i) + " "), end="")

        for j in range(x):
            if matrix[j][i].isSweeped:
                print(str(matrix[j][i].minesAround) + " ", end="")
            elif matrix[j][i].isMine:
                if j == x_ and i == y_:
                    print(strBoldRed("x "), end="")
                else:
                    print("x ", end="")
            elif matrix[j][i].isFlag:
                print(strYellow("? "), end="")
            else:
                print("- ", end="")
        print()
    print("y")
    print()

def sweepPixel(x_, y_):
    if matrix[x_][y_].isMine:
        printGameoverMatrix(x_, y_)
        exit()
    matrix[x_][y_].isSweeped = True
    minesAround = matrix[x_][y_].minesAround = getMinesAround(x_, y_)
    if minesAround == 0:
        range = [-1, 0, 1]
        for i in range:
            for j in range:
                x_tmp = x_ + i
                y_tmp = y_ + j
                if not (y_tmp >= y or x_tmp >= x or y_tmp < 0 or x_tmp < 0 or matrix[x_tmp][y_tmp].isSweeped):
                    sweepPixel(x_tmp, y_tmp)
    return

def isWon():
    condition1 = True
    condition2 = True
    for i in range(x):
        for j in range(y):
            if matrix[i][j].isMine != matrix[i][j].isFlag:
                condition1 = False
            if matrix[i][j].isMine == matrix[i][j].isSweeped:
                condition2 = False
            if not(condition1 or condition2):
                return False
    return True

while True:
    printMatrix()

    # check if the user has won
    if isWon():
        print("\nYou won!")
        exit()

    # user input
    input_x = input("x: ")
    if ord(input_x) >= 65:
        input_x = ord(input_x.lower()) - 87
    else:
        input_x = int(input_x)
    input_y = input("y: ")
    if ord(input_y) >= 65:
        input_y = ord(input_y.lower()) - 87
    else:
        input_y = int(input_y)

    selectedPixel = matrix[input_x][input_y]

    if not(selectedPixel.isFlag or selectedPixel.isSweeped):
        option = input("\n1- Sweep\n2- Flag\n> ")
        if option == "1":
            sweepPixel(input_x, input_y)
        if option == "2":
            matrix[input_x][input_y].isFlag = True
    elif selectedPixel.isFlag:
        option = input("\n1- Sweep\n2- Unflag\n> ")
        if option == "1":
            sweepPixel(input_x, input_y)
        if option == "2":
            matrix[input_x][input_y].isFlag = False
    elif selectedPixel.isSweeped:
        print("The point is already sweeped!")
