# Password Generator by rene.jock@outlook.de
# Author: Rene Jock
# 14.06.2022

import string
import random

passlen = int(input('Wie lang soll das Passwort sein? '))
passNum = int(input('Wieviele Passwörter sollen es sein? '))


def passGen(len, num):
    for i in range(passNum):
        newPass = print(''.join(random.choice(string.ascii_letters + string.digits)
        for x in range(passlen)))
    return newPass

print('Dein Zufällig erstelltes Passwort ist: ')
passGen(passlen, passNum)    
