n=int(input(">Enter the number:"))
bol=True
for i in range(2,(n**0.5)+1):
   if n%i==0:
      bol=False
      break
   else:
      bol=True
if bol:
   print(">Is prime")
else:
   print(">Not prime")     
