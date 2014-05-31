import System.IO  
import Control.Monad
import Data.List

sumL :: (Integral a) => [a] -> a
sumL l = foldl (\x -> \y -> x + y) 0 l

main = 
  do contents <- readFile "data.txt"
--      print contents
     let strs = map readInt $ words contents
     let res = sumL strs
     print res
--     print 
--     print . map readInt . words $ contents

readInt :: String -> Integer
readInt = read
  
