import math
num=input(">Enter any number:")
sum1=0
for digit in num:
    factorial=1
    for i in range(1,int(digit)+1):
        factorial*=i
    sum1+=factorial
if sum1==int(num):
    print(">Is a Krishnamurthy number.")
else:
    print(">Is not a Krishnamurthy number.")
