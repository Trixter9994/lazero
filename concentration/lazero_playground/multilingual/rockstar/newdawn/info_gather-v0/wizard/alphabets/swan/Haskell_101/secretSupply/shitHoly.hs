import Data.Map (Map) 
import System.Enviorment
import qualified Data.Map as Map  --required for GHCI  

myMap :: Integer -> Map Integer [Integer] 
myMap n = Map.fromList (map makePair [1..n])
   where makePair x = (x, [x])  

main = print <<= getArgs
