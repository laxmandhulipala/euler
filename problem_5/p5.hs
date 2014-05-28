import Data.List as List
import Debug.Trace as Trace

largestFactor' :: (Integral a) => a -> a -> a -> [a] -> [a]
largestFactor' n cur orig facs = 
  if (cur > orig) then facs
  else 
    if mod n cur == 0 then largestFactor' (div n cur) cur orig $ facs ++ [cur]
    else largestFactor' n (cur+1) orig facs

allFacs :: (Integral a) => a -> [a]
allFacs n = 
  let
    res = largestFactor' n 2 n []
  in
    if length res == 0 then [n]
    else res

getFactorization :: (Integral a) => a -> [(a,Int)]
getFactorization n = List.map (\x -> (head x, length x)) $ List.group (allFacs n)

ourinsert :: (Integral a) => [(a,Int)] -> (a,Int) -> [(a,Int)]
ourinsert [] x = [x]
ourinsert ((y1,y2):xs) (x1,x2) = if x1 == y1 then (x1, max x2 y2):xs
                                 else (y1,y2):(ourinsert xs (x1,x2))

ourlcm :: (Integral a) => a -> a -> a
ourlcm x y = 
  let
    fx = getFactorization x
    fy = getFactorization y 
    fplus = List.sortBy (\(x1,x2) -> \(y1,y2) -> compare x1 y1) $ fx ++ fy
    fcollected = foldl ourinsert [] fplus 
  in
    foldl (\x -> \(n1,n2) -> x * (n1^n2)) 1 fcollected 

chainLcm :: (Integral a) => [a] -> a
chainLcm l = foldl ourlcm 1 l
