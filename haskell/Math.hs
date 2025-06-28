module Math (add, minus, multiplyBy, dividedBy, 
    pow, roots, fib, sqrt', fac,
    e, g, c, nan,
) where

--- Add
add :: Float -> Float -> Float
add a b = a + b
--- Add end

--- Minus
minus :: Float -> Float -> Float
minus a b = a - b
--- Minus end

--- Multiply By
multiplyBy :: Float -> Float -> Float
multiplyBy a b = a * b
--- Divided By end

--- Divided By
dividedBy :: Float -> Float -> Float
dividedBy a b = do
    if b == 0
        then 0.0
        else a / b
--- Divided By end

--- Power
pow :: Float -> Integer -> Float
pow a b = do
    if b == 0
        then 1
        else a * pow a  (b - 1)
--- Power end

--- Roots
roots :: (Float, Float, Float) -> (Float, Float)  
roots (a,b,c) = (x1, x2) where 
   x1 = e + sqrt d / (2 * a) 
   x2 = e - sqrt d / (2 * a) 
   d = b * b - 4 * a * c  
   e = - b / (2 * a)
--- Roots end

--- Fib
fib :: Int -> Int
fib n | n == 0 = 0
      | n == 1 = 1
      | n > 1 = fib (n - 1) + fib (n - 2)
--- Fib end

--- Sqrt
sqrt' :: Double -> String
sqrt' n | n >= 0 = show(sqrt n)
        | n == (-1) = "i"
        | otherwise = show(sqrt (-n)) ++ "i"
--- Sqrt end

--- Fac
fac :: Int -> Int
fac n | n == 1 || n == 0 = 1
      | n > 0 = n * fac (n - 1)
      | n < 0 = error "Factorial is not defined for negative numbers"
--- Fac end

--- Consts
e :: Double
e = 2.718281828459045

g :: Double
g = 9.8

c :: Double
c = 3e8

nan :: Double
nan = 0/0
--- Consts end

--- Custom operators
infix 9 +-
(+-) :: Int -> Int -> [Int]
a +- b = [(a - b)..(a + b)]

infixl 7 %
a % b = a `mod` b

infix 4 !=
(!=) :: Eq a => a -> a -> Bool
a != b = do
    if a /= b 
        then True
        else False
--- Custom operators end