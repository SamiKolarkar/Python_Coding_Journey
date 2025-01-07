n=int(input(">Enter the nth number:"))
n1=0
n2=1
print(">The Series is:")
for i in range(n):
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
print(">The sum of the series is:",n3-1)
print(">The last number is :",n2-n1)
