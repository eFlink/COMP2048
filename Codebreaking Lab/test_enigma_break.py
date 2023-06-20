# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import string
import enigma
import rotor

letters = string.ascii_letters  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
# print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. " \
                        "Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo " \
                        "rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "F Hail Shakes!"
crib_substring = "Hail Shakes!"


# Break the code via brute force search
# INSERT CODE HERE

print(ShakesHorribleMessage)
message = ""
counter = 0
for c1 in string.ascii_uppercase:
    if message[-12:] == crib_substring:
        break
    for c2 in string.ascii_uppercase:
        if message[-12:] == crib_substring:
            break
        for c3 in string.ascii_uppercase:
            key = ""
            key += c1
            key += c2
            key += c3
            engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                   rotor.ROTOR_II, rotor.ROTOR_III, key,
                                   plugs="AA BB CC DD EE")
            message = engine.encipher(ShakesHorribleMessage)
            counter += 1
            if message[-12:] == crib_substring:
                break

print("done")

# Print the Decoded message
# INSERT CODE HERE

print(message)
print(counter)

