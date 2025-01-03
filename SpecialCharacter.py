char=input(">Enter any character:")
if len(char)!=0:
    if "a"<=char<="z":
        print(">Lowercase")
    elif "A"<=char<="Z":
        print(">Uppercase")
    elif "0"<=char<="9":
        print(">Digit")
    else:
        print(">Special charater")
