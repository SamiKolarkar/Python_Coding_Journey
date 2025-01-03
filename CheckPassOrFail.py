maths=int(input(">Enter marks of Maths:"))
english=int(input(">Enter the marks of English:"))
computer=int(input(">Enter the marks of Computer:"))
avg=maths+english+computer/3
if maths>=40 or english>=40 or computer>=40 or avg>=40:
    print(">You are Pass!!!")
else:
    print(">You are Fail!!!")
