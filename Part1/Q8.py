

#Palendrome String Program 
s="mkkokkm"
arr=list(s)
j=len(s)
k=0
n=0
for i in range(len(s)):
    if(arr[k+j-1]==arr[i]):
        n=n+1
    k=k-1
if(n==len(s)):
    print('String is palindrome')
else:
    print('String is not palindrome')
    

    
  

    
    


   
