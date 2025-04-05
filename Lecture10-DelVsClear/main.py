x = 10
del x
print(x) #NameError: name 'x' is not defined

list1 = [1,2,3]
list1.clear()
print(list1) # []


list2 = [10,20,30,40]
del list2[2]
print(list2) # [10, 20, 40]


list3 = [10,20,30,40]
list3[2].clear()
print(list3) # error