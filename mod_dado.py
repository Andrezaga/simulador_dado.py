from os import read
from random import randint
from mod_menu import readstring

def dice4():
    d = randint(1,4)
    print(d)
    while True:
        c = readstring('Do you want to play again? [Y/N]').strip().upper()[0]
        if c == 'Y':
            d = randint(1,4)
            print(d)
        elif c == 'N':
            break
        else:
            print('ERROR! Use only "Y" or "N" to answer.')
    
def dice6():
    d = randint(1,6)
    print(d)
    while True:
        c = readstring('Do you want to play again? [Y/N]').strip().upper()[0]
        if c == 'Y':
            d = randint(1,6)
            print(d)
        elif c == 'N':
            break
        else:
            print('ERROR! Use only "Y" or "N" to answer.')

def dice8():
    d = randint(1,8)
    print(d)
    while True:
        c = readstring('Do you want to play again? [Y/N]').strip().upper()[0]
        if c == 'Y':
            d = randint(1,8)
            print(d)
        elif c == 'N':
            break
        else:
            print('ERROR! Use only "Y" or "N" to answer.')

def dice10():
    d = randint(1,10)
    print(d)
    while True:
        c = readstring('Do you want to play again? [Y/N]').strip().upper()[0]
        if c == 'Y':
            d = randint(1,10)
            print(d)
        elif c == 'N':
            break
        else:
            print('ERROR! Use only "Y" or "N" to answer.')

def dice12():
    d = randint(1,12)
    print(d)
    while True:
        c = readstring('Do you want to play again? [Y/N]').strip().upper()[0]
        if c == 'Y':
            d = randint(1,12)
            print(d)
        elif c == 'N':
            break
        else:
            print('ERROR! Use only "Y" or "N" to answer.')

def dice20():
    d = randint(1,20)
    print(d)
    while True:
        c = readstring('Do you want to play again? [Y/N]').strip().upper()[0]
        if c == 'Y':
            d = randint(1,20)
            print(d)
        elif c == 'N':
            break
        else:
            print('ERROR! Use only "Y" or "N" to answer.')

