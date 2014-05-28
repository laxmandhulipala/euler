largestFactor' :: (Integral a) => a -> a -> a -> [a] -> [a]
largestFactor' n cur orig facs = 
  if (cur > orig) then facs
  else 
    if mod n cur == 0 then largestFactor' (div n cur) cur orig $ facs ++ [cur]
    else largestFactor' n (cur+1) orig facs

largestFactor :: (Integral a) => a -> a
largestFactor n = 
  let 
    res = largestFactor' n 2 n []
  in if length res == 0 then n 
     else last res
