# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine

# create the Turing machine
multiplier = TuringMachine(
    {
        # Write your transition rules here as entries to a Python dictionary
        # For example, the key will be a pair (state, character)
        # The value will be the triple (next state, character to write, move head L or R)
        # such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        # then transition to state q1, write a 0 and move head right.

        # Go right to the second number
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', '0'): ('q1', '0', 'R'),
        # Go right until the blank character then add seperator
        ('q1', '1'): ('q1', '1', 'R'),
        ('q1', ''): ('q2', '0', 'L'),
        # Go left until the middle character
        ('q2', '1'): ('q2', '1', 'L'),
        ('q2', '0'): ('q3', '0', 'R'),
        # Go through 2nd number to see which hasn't been processed yet
        ('q3', 'X'): ('q3', 'X', 'R'),
        ('q3', '1'): ('q4', 'X', 'L'),
        ('q3', '0'): ('qa', '', 'L'),  # if ...
        # Go left until the middle character
        ('q4', 'X'): ('q4', 'X', 'L'),
        ('q4', '0'): ('q5', '0', 'L'),
        # Parse through 1st number until unprocessed is reached
        ('q5', 'Y'): ('q5', 'Y', 'L'),
        ('q5', '1'): ('q6', 'Y', 'R'),
        ('q5', ''): ('q11', '', 'R'),  # Go to q11 once end of number is reached
        # Go right until the middle character
        ('q6', 'Y'): ('q6', 'Y', 'R'),
        ('q6', '0'): ('q7', '0', 'R'),
        # Go right until the seperator
        ('q7', '1'): ('q7', '1', 'R'),
        ('q7', 'X'): ('q7', 'X', 'R'),
        ('q7', '0'): ('q8', '0', 'R'),
        # Go right until blank to increment number by 1
        ('q8', '1'): ('q8', '1', 'R'),
        ('q8', ''): ('q9', '1', 'L'),
        # Go left until seperator to end of second number
        ('q9', '1'): ('q9', '1', 'L'),
        ('q9', '0'): ('q10', '0', 'L'),
        # Go left until end of first number then back to q5
        ('q10', '1'): ('q10', '1', 'L'),
        ('q10', 'X'): ('q10', 'X', 'L'),
        ('q10', '0'): ('q5', '0', 'L'),  # if
        # Reset first number to be unprocessed for all digits
        ('q11', 'Y'): ('q11', '1', 'R'),
        ('q11', '0'): ('q3', '0', 'R'),

        # works adding a digit for all digits in the first number every time a
        # digit from the second number is replaced with X
    }
)
print("2 * 3 =")
multiplier.debug('110111', step_limit=300)
print()
print("3 * 5 =")
multiplier.debug('111011111', step_limit=10000)

