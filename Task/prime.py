n=int(input("enter the no"))
i=2
while(n!=1):
    rem=n%i
    if(rem==0):
        n=n/i
        print(i)
    else:
         print("not a prime")