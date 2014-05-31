import math

def sieve(n):
  primes = [True]*n
  for i in xrange(4,n,2):
    primes[i] = False
  for i in xrange(3,int((n**0.5))+1,2):
    if (primes[i]):
      for j in xrange(2*i,n,i):
        primes[j] = False
  out = []
  for i in xrange(2,n):
    if (primes[i]):
      out += [i]
  return out

p = sieve(2000000)

prSum = 0
for pr in p:
  prSum += pr

print(prSum)


