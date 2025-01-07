num=input(">Enter any number:")
idx=len(num)-1
last_num=int(num[idx])
sum=0
no=0
for i in range(0,len(num)):
    no=int(num[i])
    sum=sum+(no**last_num)
if int(num)==sum:
    print(">Armstrong number.")
else:
    print(">Not a armstrong number.")
