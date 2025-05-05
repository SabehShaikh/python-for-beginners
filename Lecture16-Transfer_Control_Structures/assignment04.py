# combine all three:

# loop from 1 to 20
# if the number is divisible by 7 , break the loop
# if the number is divisible by 3, continue the loop
# if the number is even and less than 10, use pass
# print other numbers

for i in range(1,21):

    if i % 7 == 0:
        break

    if i % 3 == 0:
        continue

    if i % 2 == 0 and i < 10:
        pass

    else:
        print(i)