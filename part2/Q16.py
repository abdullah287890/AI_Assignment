#Sum of digits of number
sum=0
n=input('Enter an integer  ')
l=0
for i in range(1,len(n)+1):
   l=l+1


n=int(n)
for i in range(1,l+1):
    c=n%10
    
    n=n//10
    sum=sum+c
print(sum)
