import Data.Char

sumDigs :: (Num a, Show a) => a -> Int
sumDigs(n) = 
  let 
    l = map digitToInt $ show n
  in
    foldl (\x -> \y -> x + y) 0 l
    
