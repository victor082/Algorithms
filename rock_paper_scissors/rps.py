#!/usr/bin/python

# Establish vasriables to track wins for the player and the computer
# Get input from tuser to choose from R/P/S
# Have the computer select R/P/S randomly
# While Loop: Compare player selection and computer selection. Determine who won or a tie.
import sys


def rock_paper_scissors(n):
    def rockpaperscissorsgame(rounds):
        options = ["rock", "paper", "scissors"]
        result = []
        for round in rounds:
            for choice in options:
                newRound = round[:]
                newRound.append(choice)
                result.append(newRound)
        return result
    if n == 0:
        return [[]]
    else:
        return rockpaperscissorsgame(rock_paper_scissors(n - 1))


print(rock_paper_scissors(2))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
