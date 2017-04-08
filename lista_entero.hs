aEntero :: [Integer] -> Integer
aEntero ls = case ls of
		[] -> 0
		x:xs -> x*10^(length xs) + aEntero xs