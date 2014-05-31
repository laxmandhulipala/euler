import sys

def parseDag(fname):
  f = open(fname,'r')
  mat = [map(int, line.split()) for line in f]
  return mat

mat = parseDag("data.txt")
print mat

height = len(mat)

memo = {}

for i in xrange(height):
  memo[i] = {}

def computePath(i,j):
  width = len(mat[i])
  if (i == (height-1)):
    # leaf:
    return mat[i][j]
  elif (j in memo[i]):
    return memo[i][j]
  else:
    lchild = j
    rchild = j+1
    lres = computePath(i+1,lchild)
    rres = computePath(i+1,rchild)
    ourres = mat[i][j] + max(lres, rres)
    memo[i][j] = ourres
    return ourres

res = computePath(0,0)
print(res)
