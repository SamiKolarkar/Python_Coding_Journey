dict1={'english':56,'maths':84,'physics':92,'computer':95,'history':87,'geography':64}
list1=list(dict1.keys())
list2=list(dict1.values())
for subject in list1:
    for marks in list2:
        print(f'{subject}={marks}')
        break
