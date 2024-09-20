import time
import timeit

def find_prime_factors(n:int)->list:
    prime_factors =[]
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    
    if n > 1:
        prime_factors.append(n)     
    return prime_factors

#Take the the time how long it takes for the function to go through all numbers from t and down to 1
t = 1000000
first_start =timeit.default_timer()
while t > 0:
    find_prime_factors(t)
    t -=1
first_stop = timeit.default_timer()




def find_prime_factors_optimized(n: int) -> list:
    prime_factors = []
    
    # Handle the even numbers first(multiples of 2)
    while n % 2 == 0:
        prime_factors.append(2)
        #floor division
        n //= 2

    # Check for odd factors from 3 onwards
    i = 3
    while i * i <= n:
        while n % i == 0:
            prime_factors.append(i)
            #floor division
            n //= i
        i += 2  # Only check odd numbers, since all even numbers have been taken care of above

    # If the remaining n is a number greater than 2, append it. 1 and lower numbers are not classified as prime numbers, and the number 2 have already been taken care of
    if n > 2:
        prime_factors.append(n)
    
    return prime_factors

#Take the the time how long it takes for the function to go through all numbers from t and down to 1
t = 1000000
optimized_start =timeit.default_timer()
while t > 0:
    find_prime_factors_optimized(t)
    t -=1
optimized_stop = timeit.default_timer()

first_execution = first_stop - first_start
optimized_execution =optimized_stop - optimized_start 


print(f"Default: {first_execution}")
print("----------------------------------")
#Optimized version of the code performes better for larger numbers.
print(f"Optimized: {optimized_execution}")

print(f"Function should return an empty list []. Returns: {find_prime_factors_optimized(1)}")
print(f"Function should return [101]. Returns: {find_prime_factors_optimized(101)}")
print(f"Function should return [2, 2, 5, 5]. Returns: {find_prime_factors_optimized(100)}")
print(f"Function should return [2]. Returns: {find_prime_factors_optimized(2)}")