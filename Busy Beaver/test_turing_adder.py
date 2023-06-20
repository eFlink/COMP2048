# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine

# create the Turing machine
adder = TuringMachine(
    {
        # Write your transition rules here as entries to a Python dictionary
        # For example, the key will be a pair (state, character)
        # The value will be the triple (next state, character to write, move head L or R)
        # such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        # then transition to state q1, write a 0 and move head right.

        ('q0', '1'): ('moveRightPre', 'X', 'R'),
        ('q0', '0'): ('End', '', 'R'),

        # move right pre 0 number
        ('moveRightPre', '1'): ('moveRightPre', '1', 'R'),  # Traverse right until end of number then traverse the next
                                                            # number
        ('moveRightPre', '0'): ('moveRightPost', '0', 'R'),

        ('moveRightPost', '1'): ('moveRightPost', '1', 'R'),
        ('moveRightPost', ''): ('moveLeftPre', '1', 'L'),     # When end of number is reached add a new '1'

        ('moveLeftPre', '1'): ('moveLeftPre', '1', 'L'),
        ('moveLeftPre', '0'): ('moveLeftPost', '0', 'L'),

        ('moveLeftPost', '1'): ('moveLeftPost', '1', 'L'),
        ('moveLeftPost', 'X'): ('q0', 'X', 'R'),

        ('End', '1'): ('qa', '1', 'R')

    }
)
print("2 + 3 =")
adder.debug('110111')
print()
print("3 + 4 =")
adder.debug('11101111')
