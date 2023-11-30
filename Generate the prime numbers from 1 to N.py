def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def generate_primes(N):
    primes = []
    for i in range(1, N + 1):
        if is_prime(i):
            primes.append(i)
    return primes

N = int(input("Enter a positive integer: "))
print("The prime numbers from 1 to", N, "are:", generate_primes(N))
