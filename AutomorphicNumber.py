num=int(input(">Enter any number:\n>"))
n=str(num)
size=len(n)
sq=num**2
div=10**size
val=num%div
if val==num:
    print(">Is a automorphic number.")
else:
    print(">Not a automorphic number.")
