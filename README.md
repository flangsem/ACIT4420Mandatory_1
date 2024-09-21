# ACIT4420Mandatory_1
Link to Github repository:
https://github.com/flangsem/ACIT4420Mandatory_1

A)
In the code:


def find_prime_factors(n, prime_factors =[]):

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

There is nothing wrong with the logical operators.
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
when one calls the function and what to expect the function to return. I also added
comments to descripe what the code handles.

I devided the while loop into two different loops. One to handle all even numbers and 
one to handle all odd numbers. By doing this we can increase the rate that the 
secound while loop reqires to itterate through the possible prime factors.
In terms of big O notation it doesnt change the value from O(sqrt(n)), but for larger 
numbers quite substantialy, for larger numbers one can see that the time diference if
going towradsr half the time of the old function. 




B)
Instead of having to create three sets of the same function deposit, we use the one
created in BancAccount for all three classes. The withdraw function is the same in
BankAccount And SavingsAccount, therefore SavingAccounts innehernce of BankAccount 
lets us use BankAccounts withdraw function. ChecinngAccount however needs to have 
an additional fee on it's withdraws. Therefore it needs its own withdraw function
to add this fee. Instead of calling the function someting  else we can name the 
function the same as a childs classfunction trupmhs its parerntclass functions,
thus overriding the innherrited function.

