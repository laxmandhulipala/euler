memo = {}

def collatz(n):
  res = 0
  if (n in memo):
    return memo[n]
  elif(n == 1):
    memo[n] = 1
    return 1
  elif(n % 2 == 0):
    res = 1 + collatz(n/2)
  else: 
    res = 1 + collatz(3*n + 1)
  memo[n] = res
  return res

for i in xrange(1,1000000):
  collatz(i)

imax = 0
maxi = 0
for i in memo:
  if (maxi < memo[i]):
    imax = i
    maxi = memo[i]

print(imax)
print(maxi)
