# ACIT4420Mandatory_1

A)
In the code:
def find_prime_factors(n, prime_factors =[]):
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

there is nothing wrong with the logical operators.
There is however something illogical with the input of the function. 
As in it doesnt quite make sense to insert an empty list for each
number that one wishes to get a list of its prime factors. If one 
doesnt add the list, the previously created instance of the list is 
used and the function will return a list with all the prime factorials 
of the inputed number, as well as the prime factorials of the previous 
number. Since it is a one dimensional list the prime factorials are
simply appended to the list with nothing seperating the prime factorials
of each number if a new list is not used when calling the function.

Therefore i have moved the initialization of the list inside of the function 
instead of in its input like this:

def find_prime_factors(n: int)->list:
    prime_factors = []

For better readability of the code i added annotation of what input is expected
when one calls the function and what to expect the function to return
