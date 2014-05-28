import math

squares = {}
for i in xrange(1000):
  val = i**2
  squares[val] = True

triples = []

for i in xrange(1000):
  for j in xrange(i,1000):
    val = i**2 + j**2
    if val in squares:
      triples.append((i,j,math.sqrt(val)))

cMax = 0

for trip in triples:
  if (trip[0] + trip[1] + trip[2] == 1000):
    cMax = max(cMax, trip[0]*trip[1]*trip[2])

print(cMax)
