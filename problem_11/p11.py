import sys

mat = []
with open('data.txt', 'r') as f:
  mat = [map(int, line.split()) for line in f]


h = len(mat)
w = len(mat[0])

gmax = 0

for i in xrange(len(mat)):
  for j in xrange(len(mat[0])):
    # try row, col, and diag from mat[i][j]
    omax = 0
    r = False
    c = False
    # row
    if (j+3 < w):
      r = True
      omax = max(omax, mat[i][j] * mat[i][j+1] * mat[i][j+2] * mat[i][j+3])

    # col
    if (i+3 < h):
      c = True
      omax = max(omax, mat[i][j] * mat[i+1][j] * mat[i+2][j] * mat[i+3][j])

    # diag
    if (r and c):
      omax = max(omax, mat[i][j] * mat[i+1][j+1] * mat[i+2][j+2] * mat[i+3][j+3])

    if (j + 3 < w and i - 3 >= 0):
      omax = max(omax, mat[i][j] * mat[i-1][j+1] * mat[i-2][j+2] * mat[i-3][j+3])

    gmax = max(gmax, omax)

print(gmax)
print(mat)
