n=int(input(".Enter any number:"))
if n==1 or n==0:
    print(">",0)
else:
    i=1
    fact=1
    while i<=n:
        fact=i*fact
        i+=1
    print(">",fact)
