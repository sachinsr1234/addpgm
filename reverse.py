i=int(input("enter a number"))
sum=0
while(i>0):
    n=int(i%10)
    sum=sum*10+n
    i=int(i/10)
print(sum)


