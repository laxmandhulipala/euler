import Data.Char

fact :: (Integral a) => a -> a
fact 1 = 1
fact n = n * fact(n-1)

sumDigs :: (Num a, Show a) => a -> Int
sumDigs(n) = 
  let 
    l = map digitToInt $ show n
  in
    foldl (\x -> \y -> x + y) 0 l
