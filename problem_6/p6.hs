import Data.List

sumSquares [] r = r
sumSquares (p:ps) r = sumSquares ps (r + p^2)

squareSum [] r = r^2
squareSum (p:ps) r = squareSum ps (r + p)

calc = (squareSum [1..100] 0) - (sumSquares [1..100] 0) 
