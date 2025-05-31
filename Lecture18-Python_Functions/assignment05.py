# input a list of numbers, find the sum, max, min using sum(), max() and min():

nums = []

for i in range(3):
    num = int(input("Enter a number: "))
    nums.append(num)

print("Sum:", sum(nums))
print("Max:", max(nums))
print("Min:", min(nums))