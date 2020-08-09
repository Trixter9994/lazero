module HS01 where
-- mother fucker!
a :: Integer
a = 42
-- who the fuck needs you to clarify the goddamn type?
-- fuck you
silly :: Integer -> Integer
silly x = go x where go y = y + 2

silly' :: Integer -> Integer
-- sample shitty lambda fucker
silly' = go where go = \x -> x + 2

id :: a -> a
id x = x

const :: a -> b -> a
const x _ = x
-- this reminds me of prolog.
flip :: (a -> b -> c) -> b -> a -> c
-- what the hell is this shit?
flip f x y = f y x

generateList f x y = [f,y,x]

data RootOfQuadratic
    = TwoRoot Double Double
    | RepeatedRoot Double
    | NoRoot
    deriving Show

add a = a + 2

rootOfQuadraticEquation' :: Double -> Double -> RootOfQuadratic
rootOfQuadraticEquation' p q = case () of
    _ | d > 0 -> let sd = sqrt d in TwoRoot ((p + sd) / 2) ((p - sd) / 2)
      | d == 0 -> RepeatedRoot (p / 2)
      | otherwise -> NoRoot where d = p ** 2 - 4 * q


test :: (Integer -> Integer) -> Integer -> Integer
test f x = f (f x)
-- how to import this dumb module?