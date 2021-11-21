from random import randint
from time import sleep

#An function to create my headers
def head(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)

#An function to treat exceptions 
def readint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERROR! Use an integer number to choose.\033[m')
            sleep(1)
        else:
            return n

#An function to treat exceptions / I need help because i dont know an exception for just numbers 
def readstr(msg): 
    while True:
        try:
            n = str(input(msg))
        except:
            print(f'\033[0;31mERROR! Use an letter to choose.\033[m')
            sleep(1)
        else:
            return n 

#An function to show an menu
dices = [4,6,8,10,12,20]
def menu():
    head('RPG Dice') 
    for e, d in enumerate(dices):
        print(f'{e+1} - {d}-sided dice')
    print(f'7 - Quit')
    print('-'*30)

#An function to play the dice
def dice(n):
    d = randint(1,n)
    print(f'\033[7m  The value is {d}  \033[m')
    sleep(2)
    while True:
        c = readstr('Do you want to play again? [Y/N] ').strip().upper()
        if c == 'Y':
            d = randint(1,n)
            print(f'\033[7m  The value is {d}  \033[m')
        elif c == 'N':
            break
        else:
            print(f'\033[0;31mERROR! Use only "Y" or "N" to answer.\033[m')
        sleep(1)
                
    
