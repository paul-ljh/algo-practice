# Generate a list of primes from 1 to n
# It's based on all composites are divisible by a prime number.

from math import ceil, sqrt

def sieve_of_eratosthenes(n):
  prime_flags = [False, False, True]
  for i in range(3, n+1):
    if i % 2 == 0:
      prime_flags.append(False)
    else:
      for j in range(ceil(sqrt(i))+1):
        if prime_flags[j] and i % j == 0:
          prime_flags.append(False)
          break
      else:
        prime_flags.append(True)
  return prime_flags

def test():
  expected_prime_flags = [0,0,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0]
  print('PASS' if sieve_of_eratosthenes(20) == expected_prime_flags else 'FAIL')

if __name__ == '__main__':
  test()
