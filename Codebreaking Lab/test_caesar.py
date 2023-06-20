# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

Created on Fri Feb  1 23:06:50 2019

@author: shakes
"""
import string

letters = string.ascii_letters  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# message = "The quick brown fox jumped over the lazy dog"  # type your message here
message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr"

print("Message:", message)

# create the Caesar cypher
offset = 11  # choose your shift
totalLetters = 26
keys = {}  # use dictionary for letter mapping
invkeys = {}  # use dictionary for inverse letter mapping, you could use inverse search from original dict
for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters:  # lowercase
        shift = index - offset
        if shift < 0:
            shift += 26
        keys[letter] = letters[shift]

        shift = index + offset
        if shift >= 26:
            shift -= 26
        invkeys[letter] = letters[shift]
    else:  # uppercase
        shift = index - offset
        if shift < 26:
            shift += 26
        keys[letter] = letters[shift]

        shift = index + offset
        if shift >= 52:
            shift -= 26
        invkeys[letter] = letters[shift]

print("Cypher Dict:", keys)
print("Cypher Dict reverse:", invkeys)


# encrypt
encryptedMessage = []
for letter in message:
    if letter == ' ':  # spaces
        encryptedMessage.append(letter)
    else:
        encryptedMessage.append(keys[letter])
print("Encrypted Message:", ''.join(encryptedMessage))  # join is used to put list inot string

# decrypt
decryptedMessage = []
for letter in encryptedMessage:
    if letter == ' ':  # spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage))  # join is used to put list inot string
