import System.Enviroment
-- i am not afraid of forgetting.
-- i never forget. i never forgive.
-- greeting :: String
-- greeting = ["shit","happens"]
-- check the thing
-- asshole :: IO ()
-- decide whether it misses anything or not.
-- they must be separated, if possible change it into a tuple
-- seriously it doesn't mean shit
-- nothing is too crazy. you are just not aware of it.
t lst = (length (filter (\x -> x>='0' && x<= '9') lst)) == length lst
t0 lst = [(x,t x)|x <-lst]
main = do
  a <- getArgs
  b <- t0 a
  print a
  print b
