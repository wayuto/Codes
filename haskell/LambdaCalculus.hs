true = \x y -> x
false = \x y -> y
no = \b -> (\b x y -> b x y) b (\x y -> y) (\x y -> x)

main :: IO ()
main = do
    putStrLn $ show (no true 1 0)