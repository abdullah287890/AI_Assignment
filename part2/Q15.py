#even odd number sun
even,odd=0,0
n=int(input('Enter a number   '))
for i in range(1,n+1):
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
print('Even numbers are   ',even)
print('Odd numbers are   ',odd)