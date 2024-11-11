a=int(input('Enter side 1'))
b=int(input('Enter side 2'))
c=int(input('Enter side 3'))

if (a==b==c):
    print('This is an equilateral triangle')
elif (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
    print('This is isosceles tringle')
else:
    print('This is scalene tringle')