# -*- coding: utf-8 -*-
"""
Busy beaver Turing machine with 2 states.

Created on Sat Mar 30 13:55:25 2019

@author: shakes
"""
from turing_machine import TuringMachine

# create the Turing machine
# Part C
bbeaver2card = TuringMachine(
    {
        # Write your transition rules here as entries to a Python dictionary
        # For example, the key will be a pair (state, character)
        # The value will be the triple (next state, character to write, move head L or R)
        # such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        # then transition to state q1, write a 0 and move head right.

        # first card
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('b', '1', 'L'),

        # second card
        ('b', '0'): ('a', '1', 'L'),
        ('b', '1'): ('h', '1', 'R')

    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)
print("2-state busy beaver:")
bbeaver2card.debug('00000000000000', step_limit=1000)
print()
# Part D
# This is already the known 2-card busy beaver program

# Part E
# 3 Card
bbeaver3card = TuringMachine(
    {
        # Write your transition rules here as entries to a Python dictionary
        # For example, the key will be a pair (state, character)
        # The value will be the triple (next state, character to write, move head L or R)
        # such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        # then transition to state q1, write a 0 and move head right.

        # first card
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('h', '1', 'R'),

        # second card
        ('b', '0'): ('c', '0', 'R'),
        ('b', '1'): ('b', '1', 'R'),

        # third
        ('c', '0'): ('c', '0', 'L'),
        ('c', '1'): ('a', '1', 'L')
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)
print("3-state busy beaver:")
bbeaver3card.debug('00000000000000', step_limit=1000)
print()

# 4 Card
bbeaver4card = TuringMachine(
    {
        # Write your transition rules here as entries to a Python dictionary
        # For example, the key will be a pair (state, character)
        # The value will be the triple (next state, character to write, move head L or R)
        # such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        # then transition to state q1, write a 0 and move head right.

        # first card
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('b', '1', 'L'),

        # second card
        ('b', '0'): ('a', '1', 'L'),
        ('b', '1'): ('c', '0', 'L'),

        # third card
        ('c', '0'): ('b', '1', 'R'),
        ('c', '1'): ('h', '1', 'L'),

        # fourth card
        ('d', '0'): ('d', '1', 'R'),
        ('d', '1'): ('a', '0', 'R')
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)
print("4-state busy beaver:")
bbeaver4card.debug('00000000000000', step_limit=1000)
print()

# Part F
bbeaver5card = TuringMachine(
    {
        # Write your transition rules here as entries to a Python dictionary
        # For example, the key will be a pair (state, character)
        # The value will be the triple (next state, character to write, move head L or R)
        # such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        # then transition to state q1, write a 0 and move head right.

        # first card
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('c', '1', 'L'),

        # second card
        ('b', '0'): ('c', '1', 'R'),
        ('b', '1'): ('e', '1', 'R'),

        # third card
        ('c', '0'): ('d', '1', 'R'),
        ('c', '1'): ('a', '1', 'L'),

        # fourth card
        ('d', '0'): ('a', '1', 'L'),
        ('d', '1'): ('e', '1', 'R'),

        # fifth card
        ('e', '0'): ('b', '1', 'R'),
        ('e', '1'): ('h', '1', 'R')
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)
print("5-state busy beaver:")
bbeaver5card.debug('00000000000000', step_limit=10000)
