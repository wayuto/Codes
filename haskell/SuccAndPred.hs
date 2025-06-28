{-# LANGUAGE RankNTypes #-}

type Church = forall a. (a -> a) -> a -> a

zero :: Church
zero = \f x -> x

suc :: Church -> Church
suc n = \f x -> f (n f x)

pre :: Church -> Church
pre n = \f x -> n (\g h -> h(g f)) (\_ -> x) (\u -> u)

toChurch :: Int -> Church
toChurch 0 = zero
toChurch n = suc (toChurch (n-1))

fromChurch :: Church -> Int
fromChurch n = n (+1) 0

main :: IO ()
main = do
    let cases = [0..10]

    putStrLn "Testing results:"
    mapM_ (\n -> do
        let ch = toChurch n
        let p = pre ch
        let s = suc ch
        putStrLn $ show (fromChurch p) ++ " -> " ++ show (fromChurch ch) ++ " -> " ++ show (fromChurch s)) cases
