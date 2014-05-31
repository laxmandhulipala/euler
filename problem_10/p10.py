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
#    if (primes[
#    l = filter(lambda x: x % filterBy != 0, l)
#    primes += [filterBy]
#  return primes
#    return sieve(l, primes + [filterBy])
#  for i in xrange(len(l)):

#p = sieve(range(3,200000,2), [])

p = sieve(2000000)
#print(p)

prSum = 0
for pr in p:
  prSum += pr

print(prSum)


