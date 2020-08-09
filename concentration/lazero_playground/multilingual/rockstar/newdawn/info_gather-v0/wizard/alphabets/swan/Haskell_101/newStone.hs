import Control.Exception
main = do
 russia <- try (evaluate (div 5 0)) :: IO ( Either SomeException Int )
 case russia of
  Left ex -> putStrLn $ " Caught E!"++ show ex
  Right  v  ->   putStrLn $ " Result: " ++ show v
