n=int(input("enter number"))
s=0
n1=n
while(n>0):
    d=n%10
    s=s+d*d*d
    n=n//10
   
if s==n1:
    print("number is Armstrong")
else:
    print("number is not Armstrong")   
   
