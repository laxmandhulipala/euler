import math

def sieve(n):
  primes = [True]*n
  for i in xrange(4,n,2):
    primes[i] = False
  for i in xrange(3,int((n**0.5))+1,2):
    if (primes[i]):
      # don't void out i
      for j in xrange(2*i,n,i):
        primes[j] = False
  out = []
  for i in xrange(2,n):
    if (primes[i]):
      out += [i]
  return out

primes = sieve(100000)
dums = [""]*len(primes)

primes = dict(zip(primes, dums))

def rem_fact(n,c):
  times = 0
  while(n % c == 0):
    n /= c
    times += 1
  return (n, times)

def factorize(n):
  facts = []
  while (n != 1):
    for p in primes:
      if (n % p == 0):
        (res,times) = rem_fact(n,p)
        n = res
        facts += [(p,times)]
  return facts

def genDivisors(l):
  divs = {1:""}
  for (k,times) in l:
    for i in xrange(1,times+1):
      newVals = []
      for val in divs:
        newVals += [val*k]
      for val in newVals:
        divs[val] = ""
  return divs


divs = 0
trNum = 1
i = 2
while divs < 500:
  trNum += i
  i += 1
  print(trNum)
  facts = factorize(trNum)
  divs = max(divs, len(genDivisors(facts)))
  print(trNum, divs)
#
#print(factorize(28))
#print(genDivisors(factorize(28)))

print(trNum)


