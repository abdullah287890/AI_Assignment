guessed=9
b=False
while(b!=True):
    i=int(input('Enter number:   '))
    if i==guessed:
        print('Right Guess')
        b=True
    else:
        print('Wrong Guess')