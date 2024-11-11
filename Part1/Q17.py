n=int(input('Enter a number'))
if (n%2 and n%3):
    print('Number is divisible by both 2 and 3')
elif(n%2):
    print('Number is divisible by 2')
elif(n%3):
    print('Number is divisible by 3')
else:
    print('Number is not divisible either by 2 or 3')