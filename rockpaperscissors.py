#################################### pre cursor ####################################
# a = int(input('Enter a number:'))
# if a > 10:
#    print('yay!')
# else: 
#    print('nooooo')

#################################### build game ####################################

in1= input('Player 1: Enter your attack! ')
in2= input('Player 2: Enter your attack! ')


if in1 == ('rock'):
    if in2 == ('rock'):
        print('TIE!!!!!!')
    elif in2 == ('paper'):
        print('Player 2, you win! :-)')
    elif in2 == ('scissors'):
        print('Player 1, you win! :-)')

elif in1 == ('paper'): 
    if in2 == ('paper'): 
        print('TIE!!!!!!')
    elif(in2) == ('rock'):
        print('Player 1, you win! :-)')
    elif(in2) == ('scissors'):
        print('Player 2, you win! :-)')

if in1 == ('scissors'):
    if in2 == ('scissors'):
        print('TIE!!!!!!!!')
    elif(in2)==('rock'):
        print('Player 2, you win! :-)')
    elif(in2) == ('paper'):
        print('Player 1, you win! :-)')


