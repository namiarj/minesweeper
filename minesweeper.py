#! /usr/bin/python3

import random

def strBoldRed(str):
    return "\x1b[1;31m" + str + "\x1b[0m"

def strYellow(str):
    return "\x1b[33m" + str + "\x1b[0m"

class minePixel:
    isMine = False
    isFlag = False
    isSweeped = False
    minesAround = 0

x = 10
y = 10
mines = 20

matrix = [[minePixel() for i in range(x)] for j in range(y)]

# putting mines randomly in points
counter = 0
while counter < mines:
    rand_x = random.randint(0, x - 1)
    rand_y = random.randint(0, y - 1)
    if not matrix[rand_x][rand_y].isMine:
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

def printMatrix(isGameOver = False, x_ = -1, y_ = -1):
    if isGameOver:
        print(strBoldRed("\nGame Over!"))

    # x axis
    print("\n  ", end="")
    for j in range(x):
        print(strBoldRed(str(j) + " "), end="")
    print()

    for i in range(y):
        print(strBoldRed(str(i) + " "), end="")
        for j in range(x):
            if matrix[j][i].isSweeped:
                print(str(matrix[j][i].minesAround) + " ", end="")
            elif isGameOver and matrix[j][i].isMine:
                if j == x_ and i == y_:
                    print(strBoldRed("x "), end="")
                else:
                    print("x ", end="")
            elif matrix[j][i].isFlag:
                print(strYellow("? "), end="")
            else:
                print("- ", end="")
        print()

def sweepPixel(x_, y_):
    if matrix[x_][y_].isMine:
        printMatrix(True, x_, y_)
        exit()
    matrix[x_][y_].isSweeped = True
    value = matrix[x_][y_].minesAround = getMinesAround(x_, y_)
    if value == 0:
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
    input_x = int(input("x: "))
    input_y = int(input("y: "))

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
