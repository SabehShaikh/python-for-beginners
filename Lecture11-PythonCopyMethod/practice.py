list1 = [1,2,3,4,5]

list2 = list1.copy()

# modifying the copied list
list2.append(6)

# printing both lists:
print("Original list:", list1)
print("Copied list:", list2)

# Another example:

lis1 = ['apple' , 'banana' , 'Orange']

lis2 = lis1.copy()
print("The new lis2 is created: ", lis2)

lis2.append('Mango')
print("New Lis2 after append: ", lis2)

print("Original lis1: ", lis1)

# Another example with List inside list:

original_list = [1,2,[3,4,5],6,7]

copied_list = original_list.copy()

copied_list[2][0] = 10

print("Original list:", original_list)
print("Copied list:", copied_list)