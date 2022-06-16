#Password Generator 2 by rene.jock@outlook.de
import random

print('Willkommen bei meinem ersten Passwort Generator.')
print('Ich stelle dir nun ein paar Fragen um dein Passort erstellen zu können.')

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTOVWXYZ"
lowercase_letters = uppercase_letters.lower()
numbers = "0123456789"
spacials ="_!.:;,?!-#*"
len = int(input('Wie lang soll dein Passwört sein?(Maximale Größe: 30 Zeichen) '))
amount = 5
upper, lower, sym, num = True, True, True, True
all_char = ""

up = input('Möchtest du Großbuchstaben im Passwort?(y/n) ')

if up == 'y':
    upper = True
elif up == 'n':
    upper = False
else:
    print('Eingabe nicht erkannt, bitte Programm neustarten. Danke')

low = input('Möchtest du kleine Buchstaben im Passwort?(y/n) ')

if low == 'y':
    lower = True
elif low == 'n':
    lower = False
else:
    print('Eingabe nicht erkannt, bitte Programm neustarten. Danke')

digits = input('Möchtest du Zahlen im Passwort?(y/n) ')

if digits == 'y':
    num = True
elif digits == 'n':
    num = False
else:
    print('Eingabe nicht erkannt, bitte Programm neustarten. Danke')

syms = input('Möchtest du Sonderzeichen im Passwort?(y/n) ')

if syms == 'y':
    sym = True
elif syms == 'n':
    sym = False
else:
    print('Eingabe nicht erkannt, bitte Programm neustarten. Danke')

if upper:
    all_char += uppercase_letters
if lower:
    all_char += lowercase_letters
if sym:
    all_char += spacials
if num:
    all_char+= numbers

for i in range(amount):
    password = "".join(random.sample(all_char, len))

print('Dein neues Passwort: ' + password)