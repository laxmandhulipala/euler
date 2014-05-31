import sys

def getVal(n):
  chars = list(n)
  chars = [ord(c) - 64 for c in chars]
  res = reduce(lambda a,d: a+d, chars)
  return res

def parse(fname):
  f = open(fname, 'r')
  s = f.read()
  s = s.split(',')
  s = [a[1:-1] for a in s]    

  s.sort()
  tot = 0
  for i in xrange(len(s)):
    el = s[i]
    res = getVal(el)
    res *= (i + 1)
    tot += res
  return tot


print(parse("names.txt"))
print(getVal("COLIN"))
