# write loop from 1 to 100. Print only the number divisible by 3 
# by skipping other numbers using continue statement

for i in range(1, 101):

    if i % 3 != 0:

        continue
    
    print(i)