
def title(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)

def readint(msg):
    try:
        n = int(input(msg))
    except (ValueError)(TypeError):
        print('ERROR! Use an integer number to choose.')
    else:
        return n

def readstring(msg):
    try:
        n = str(input(msg))
    except (ValueError)(TypeError):
        print('ERROR! Use an letter to choose.')
    else:
        return n 

dices = [4,6,8,10,12,20]

def menu():
    title('RPG Dice') 
    for e, d in enumerate(dices):
        print(f'{e+1} - {d}-sided dice')
    print('7 - quit')
    print('-'*30)
    
            
    
