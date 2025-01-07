num=int(input(">Enter any number:"))
rev=0
temp=num
while(temp!=0):
    rem=temp%10
    rev=rev*10+rem
    temp//=10
if rev==num:
    print(">Entered number is a palindrome.")
else:
    print(">Entered number is not a palindrome.")
