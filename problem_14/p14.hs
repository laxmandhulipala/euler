collatz :: (Integral a) => a -> [a]
collatz 1 = [1]
collatz n = 
  if mod n 2 == 0 then n : collatz(div n 2)
  else n : collatz(3*n+1)
