str=input(">Enter any sentence:")
convert=""
for i in range(0,len(str)):
    if str[i].isupper():
        convert+=str[i].lower()
    elif str[i].islower():
        convert+=str[i].upper()
print(">",convert)
