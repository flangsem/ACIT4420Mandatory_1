
def find_prime_factors(n:int, prime_factors =[])->list:
    if n <= 1:
        return prime_factors
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1

    prime_factors.append(n)     
    return prime_factors


print(f"Primefactors of 1: {find_prime_factors(1, prime_factors=[])}")
print(f"Primefactors of 3: {find_prime_factors(3, prime_factors=[])}")
print(f"Primefactors of 10: {find_prime_factors(10, prime_factors=[])}")
print(f"Primefactors of 101: {find_prime_factors(101, prime_factors=[])}")
print(f"Primefactors of : {find_prime_factors(10103, prime_factors=[])}")
print(f"Primefactors of : {find_prime_factors(10111111111, prime_factors=[])}")

