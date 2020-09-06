main =do
 putStrLn "Hello world"
 main0
 main0
 print ( fact 6 )
{-short comment is it true?
 -just some short comments here
some short comments here
some short comments here
some short comments here
 - -}
-- comment line here
main0 = print "Hello world again!"
-- philosopher's favourite.
-- fact :: Int -> Int
--  without the definition.
fact :: Integral a  => a->a
fact n|n==0 =1
      |n/=0 =n*fact(n-1)
--fact x = x * fact ( x-1)
