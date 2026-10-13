def primes_up_to_n(n: int)->list[int]:
    not_prime=list()
    primes=list()
    for x in range(2, n):
        if x in not_prime:
            continue
        primes.append(x)
        count=2
        while count*x<n:
            not_prime.append(count*x)
            count+=1
    return primes

print(primes_up_to_n(100))

"""Return type in c++ is a vector, but in python it is a list """