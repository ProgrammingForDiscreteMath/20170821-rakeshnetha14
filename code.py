
# Create a list with the first ten triangular numbers
# (see https://oeis.org/A000217)

L = [(i*(i+1)/2) for i in range(10)]
L
# Create a function to test if a number is prime
def is_prime(n):
    """
    Test if ``n`` is a prime.
    """
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                return("False");
                break;
        else:
            return("True")
    else:
        return ("False")
                    

# Tests
# is_prime(2033) == False
# is_prime(2039) == True

is_prime(2033)
is_prime(2039)

# Create a function which returns a list of the first ten prime numbers
# greater than or equal to n

def next_ten_primes(n):
    """
    Return the list of the first ten prime numbers greater than or equal to n

    
    """
    L1=[];
    for i in range(10):
        while (is_prime(n)!='True'):
            n=n+1;
        L1=L1+[n];
        n=n+1;
    return L1
            
next_ten_primes(2033)
next_ten_primes(2039)
    


# Tests
# next_ten_primes(2033) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]
# next_ten_primes(2039) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]

