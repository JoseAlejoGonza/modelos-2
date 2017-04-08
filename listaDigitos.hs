lista:: Int -> [Int]
lista 0 = []
lista x = (mod x 10): lista(div x 10)  