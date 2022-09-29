"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f"Value {number_of_primes} is invalid. Please choose a number greater than 0")
    list = []
    number = 2
    while len(list) < number_of_primes:
        prime = True
        for i in range(2, number):
            if (number % i == 0):
                prime = False
        if prime:
            list.append(number)
        number = number + 1
    return list
