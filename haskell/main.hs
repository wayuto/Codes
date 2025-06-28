infix 9 +-

(+-) :: Int -> Int -> [Int]
a +- b = [(a - b)..(a + b)]

main :: IO ()
main = do
    let i = 10 +- 5
    print i