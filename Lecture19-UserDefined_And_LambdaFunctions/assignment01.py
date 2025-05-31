# write a function that checks whether a given number n
# is a prime number or not. A prime number is a number that
# is greater than 1 that has no divisors other 
# than 1 and itself. The function should return true if the 
# number is prime , false otherwise

def is_prime(n):

    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
