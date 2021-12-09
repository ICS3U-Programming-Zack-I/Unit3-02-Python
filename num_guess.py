#!/usr/bin/env python3
# Created by: Zack Isingoma
# Created on: Sept 08th, 2021
# This program eneables users guess number
# Guessing random number
import constants


def main():
    # this function checks if there is over 30 students
    # input
    number = int(input("Guess a number between 0 and 9: "))
    print("")

    # process & output
    if number == constants.FAVORITE_NUMBER:
        print("Good job")
    else:
        print("Wrong number")


if __name__ == "__main__":
    main()
