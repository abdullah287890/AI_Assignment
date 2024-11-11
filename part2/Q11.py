#Reverse of a number
n=123456788
u=''
for i in range(1,10):
    c=n%10
    u=u+str(c)
    n=n//10
print(u)