-- comment is it so?
-- with qualified keyword the code can get convoluted like java.
import qualified MyFirstModule
main :: IO ()
main = do
  putStrLn "Enter Your Name!"
  name <- getLine
  let message = MyFirstModule.myFirstFunction name
  putStrLn message
  let arghFuck=(\x -> x*2) 5
  print arghFuck
