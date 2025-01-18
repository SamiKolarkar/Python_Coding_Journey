a={'maths':84,'physics':92,'computer':76,'history':87,'geography':64}
list1=['maths','geography','history']
new_dict={}
for i in list1:
    if i in a:
        del a[i]
print(a)
