''' Here, we use the Sieve of Eratosthenes up to a given number to generate that number's prime
    factorisation. '''

''' This part defines the Sieve of Eratosthenes, which is used to generate all of the primes (*and*,
    in this form, all of the composites as well!) up to n. This will be used in this and future
    problems. '''

''' Note that this function returns a (nested) list; this list acts normally the way tuples do! For
    example, sieve_of_eratosthenes(131)[0] will give the list of primes up to 131,
    whereas sieve_of_eratosthenes(131)[1] will give the list of composites up to 131. If the return
    statement is replaced from return [prime_list, sieve_net] to return (prime_list, sieve_net), this
    function will return a *tuple* instead of a nested list! '''

def sieve_of_eratosthenes(n):
    prime_list = []
    sieve_net = []
    for i in xrange(2, n+1):
        if i not in sieve_net:
            prime_list.append(i)
            for j in xrange(i**2, n+1, i):
                sieve_net.append(j)
    return [prime_list, sieve_net]

''' This generates the actual list of prime factors of the number of interest, sorted in order from 
    smallest to largest. '''

def prime_factorisation(k):
    prime_factors_of_k = []
    prime_factorisation_of_k = []
    primes_up_to_k = sieve_of_eratosthenes(k)[0]
    for l in primes_up_to_k:
        if k % l == 0:
            prime_factors_of_k.append(l)
            prime_power = 1
            m = k / l
            while m % l == 0:
                prime_power += 1
                m = m / l
            prime_factorisation_of_k.extend([l]*prime_power)
    prime_factors_of_k.sort()
    prime_factorisation_of_k.sort()
    return [prime_factors_of_k, prime_factorisation_of_k]
