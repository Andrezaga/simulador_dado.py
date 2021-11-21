import mod_dado
import mod_menu
from time import sleep

while True:
    mod_menu.menu()
    n = mod_menu.readint('Choose a number to use the dice: ')
    if n == 1:
        mod_dado.dice4
    elif n == 2:
        mod_dado.dice6
    elif n == 3:
        mod_dado.dice8
    elif n == 4:
        mod_dado.dice10
    elif n == 5:
        mod_dado.dice12
    elif n == 6:
        mod_dado.dice20
    elif n == 7:
        print('Finishing... See you in the next match ;)')
        break
    else:
        print('ERROR! Use only the numbers in the list to choose a dice')
    sleep(2)

