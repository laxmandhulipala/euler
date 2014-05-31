nums = {0:"",1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 
        6:"six", 7:"seven", 8:"eight", 9:"nine"}

tens = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty",
        6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}


teens = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",
        15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 
        19:"nineteen"}

def writeNum(n):
  chars = 0
  outStr = ""
  n = str(n)
  if (n == "1000"):
    print("one thousand")
    return len("one thousand")
  if (int(n) > 99):
    chars += len("hundred")
    chars += len(nums[int(n[0])])
    outStr += "hundred"
    outStr += nums[int(n[0])]
    n = n[1:]
    if (int(n) > 0):
      chars += len("and")
      outStr += "and"
  if (int(n) > 19):
    chars += len(tens[int(n[0])])
    chars += len(nums[int(n[1])])
    outStr += tens[int(n[0])]
    outStr += nums[int(n[1])]
  elif (int(n) >= 10):
    chars += len(teens[int(n)])
    outStr += teens[int(n)]
  else:
    n = str(int(n))
    chars += len(nums[int(n[0])])
    outStr += nums[int(n[0])]
  print(outStr)
  return chars

sm = 0
for i in xrange(1,1001):
  c = writeNum(i)
  sm += c

print(sm)
