import math

def choose(n,c):
  return math.factorial(n) / (math.factorial(n-c) * math.factorial(c))
