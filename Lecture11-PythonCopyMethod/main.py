#immutable objects (mumbers, strings, tuples...)

orig_list = [1, 'hello' , (20,30)]
new_list = []

new_list = orig_list.copy()

# new list changed , not original list
new_list[1] = 'world'

# new_list[2][0] = 25 # not possible changes inside tuple

print("Original list" , orig_list)
print("New list" , new_list)

my_set = {1,2,3}

my_set.add(4)
my_set.remove(2)

print(my_set)

#Tuples
my_set = (1,2,3) # tuple

my_set.add(4) # not possible
my_set.remove(2) #not possible

print(my_set)