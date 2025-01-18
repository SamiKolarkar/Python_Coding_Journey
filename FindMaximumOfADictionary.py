dict1={'english':56,'maths':84,'physics':92,'computer':95,'history':87,'geography':64}
subject=max(dict1,key=dict1.get)
print(">The subject with maximum marks is:",subject)
