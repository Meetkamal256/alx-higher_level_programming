# ----------- A PROGRAM THAT RETURNS A LIST OF PRIMES---------------
# A prime can only be divided by 1 and itself
# 5 is prime because 1 and 5 are its only positive factors
# 6 is a composite because it is divisible by 1, 2, 3 and 6
# -----------------------------------------------------------------

# We'll receive a request for primes up to the input value
# We'll then use a for loop and check if modulus == 0 for
# every value up to the number to check
# If modulus == 0 that means the number isn't prime
def is_prime(num):  # function handles checking if a number is a prime number
    for i in range(2, num):  # a loop that circle through primes from 2 to value we need to check
        if (num % i) == 0:  # check if any division has no remainder
            return False  # return false if there is, meaning it's not a prime number
        return True  # it is a prime number


def getPrimes(max_number): # a function that deals with getting a prime number list

    list_of_primes = []  # create a list

    for num1 in range(2, max_number):
        if is_prime(num1):
            list_of_primes.append(num1)

        return list_of_primes


max_num_to_check = int(input("Search for primes up to: "))
list_of_primes = getPrimes(max_num_to_check)
for prime in list_of_primes:
    print(prime)






