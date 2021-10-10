#MENU
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#TITLE
def title():
    print('+===+'*3)
    print(' Jogo da Velha')
    print('+===+'*3)

#MENU
def menu():
    title()
    choice = int(input('''MENU
[1] PLAY
[2] HOW TO PLAY
[0] EXIT
: '''))
    if choice == 1:
        players()
    elif choice == 2:
        htp()
    elif choice == 0:
        quit()
    else: 
        print('Please, try again!')
        menu()
    
#MENU - PLAYERS
def players():
    print('')
    choice = int(input('''PLAYERS
[1] 1 PLAYER
[2] 2 PLAYERS
[0] BACK
: '''))
    if choice == 1:
        symb()
    elif choice == 2:
        pass
    elif choice == 0:
        menu()
    else:
        print('Please, try again!')
        players()
    
#MENU - PLAYERS - SYMBOL
def symb():
    print('')
    print('PLAYER 1, CHOOSE YOUR SYMBOL')
    sym = input(''' 
    [ X ] [ O ]
: ''')
    if sym == 'X' or sym == 'x':
        pass
    elif sym == 'O' or sym == 'o':
        pass

#MENU - HOW TO PLAY
def htp():
    print('')
    print('''"Whoever completes all 
spaces with their symbol 
first wins"''')
    choice = int(input('''[0] BACK
: '''))
    if choice == 0: 
        menu()
    else:
        print('Please, try again!')
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

#GAME
#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
def interface():
    a = 1
        


def main():
    menu()
    
interface()
