def nextPrime(primes, cur):
  for p in primes:
    if (cur % p == 0):
      return nextPrime(primes, cur+1)
  return cur

def getNthPrime(n):
  p = 2
  primes = [2]
  for i in xrange(n):
    p = nextPrime(primes, p)
    primes.append(p)
  print(p)
  print(len(primes))

getNthPrime(10000)
