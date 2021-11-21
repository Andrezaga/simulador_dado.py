import mod_dice
from time import sleep

while True:
    mod_dice.menu()
    n = mod_dice.readint('Choose a number to use some dice: ')
    if n == 1:
        mod_dice.dice(4)
    elif n == 2:
        mod_dice.dice(6)
    elif n == 3:
        mod_dice.dice(8)
    elif n == 4:
        mod_dice.dice(10)
    elif n == 5:
        mod_dice.dice(12)
    elif n == 6:
        mod_dice.dice(20)
    elif n == 7:
        print('Finishing... See you in the next match ;)')
        break
    else:
        print(f'\033[0;31mERROR! Use only the numbers in the list to choose a dice\033[m')
        sleep(1)
    sleep(1)

