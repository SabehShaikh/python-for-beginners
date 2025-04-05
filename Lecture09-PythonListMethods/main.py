#Append(item) --> Add an item to the end of the list

List1 = ["Apple" , "Banana" , "Orange"]

List1.append("Cherry")

print(List1)


List1 = ["Apple" , "Banana" , "Orange"]
List2 = ["Mango" , "Watermelon"]

List1.append(List2)

print(List1)

# Extend(item) --> Add multiple items to the end of the list

List1 = ["Apple" , "Banana" , "Orange"]
list2 = ["Mango" , "Watermelon"]

List1.extend(list2)

print(List1)

# Insert(index , item) --> Add an item at a specified index

List1 = ["Apple" , "Banana" , "Orange"]
List1.insert(1 , "Cherry")

print(List1)

# Remove(item) --> Remove an item from the list

List1 = ["Apple" , "Banana" , "Orange"]
List1.remove("Banana")

print(List1)

# Pop(index) --> Remove an item from a specified index

List1 = ["Apple" , "Banana" , "Orange"]
List1.pop(1) 
# If you don't specify an index,
# the pop() method removes the last item
print(List1)

# Clear() --> Remove all items from the list

List1 = ["Apple" , "Banana" , "Orange"]
List1.clear()
print(List1)

# index(item, start, end) --> Return the index of an item

List1 = ["Apple" , "Banana" , "Orange"]
x = List1.index("Banana")
print(x)

# Count(item) --> Return the number of times an item appears in the list

List1 = ["Apple" , "Banana" , "Orange" , "Banana"]
x = List1.count("Banana")
# returns 0 if the item is not in the list
print(x)

# Sort() --> Sort the list in ascending order (small to big)

Numbers = [10, 5, 30, 25, 50]
Numbers.sort()
print(Numbers)

# Sort reverse --> Sort the list in descending order (big to small)

Numbers = [10, 5, 30, 25, 50]
Numbers.sort(reverse = True)
print(Numbers)

# reverse() --> Reverse the order of the list

Numbers = [25, 50, 30, 25, 80]
Numbers.reverse()
print(Numbers)