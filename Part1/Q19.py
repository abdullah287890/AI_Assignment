s=input('Enter a word')
u,l=False,False
for i in s:
    if i>='A' and i<='Z':
        
    else:
        print('Lowercase')
if(u==True and l==True):
    print('MIX')
elif(u==True and l==False):
    print('Uppercase')
else:
    print('Lowercase')