p=int(input('Enter your percentage'))
if(p>90):
    print('Grade is A+')
elif(p>80 and p<90):
    print('Grade is A')
elif(p>70 and p<80):
    print('Grade is B')
elif(p>60 and p<70):
    print('Grade is C')
elif(p>50 and p<60):
    print('Grade is D')
elif(p>40 and p<50):
    print('Grade is E')
else:
    print('Grade is F')