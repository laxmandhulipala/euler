pallins = []
for i in xrange(10):
  for j in xrange(10):
    for k in xrange(10):
      s1 = str(i) + str(j) + str(k) + str(j) + str(i)
      num = int(s1)
      pallins.append(num)

      s2 = str(i) + str(j) + str(k) + str(k) + str(j) + str(i)
      num = int(s2)
      pallins.append(num) 

print(len(pallins))

divOfTwo = []

for palin in pallins:
  for i in xrange(100, 1000):
    if (palin % i == 0):
      res = palin / i
      if (res > 99 and res < 1000):
        divOfTwo.append(palin)

print(len(divOfTwo))
print(max(divOfTwo))
