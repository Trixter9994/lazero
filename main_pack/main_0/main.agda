module main where

data ℕ : Set where 
  zero : ℕ
  suc  : ℕ → ℕ
-- function is not datatype.
_+_ : ℕ → ℕ → ℕ 
zero + zero = zero
zero + n    = n
(suc n) + n′ = suc (n + n′)  -- use \' to input ′.

open import IO
main = run (putStrLn "this is the main lazero program.")
-- what is the difference? I mean really, agda-mode and agda itself.
-- you shall really check that component.
-- include path! -i /usr/share/agda-stdlib/ ... colons???
-- people rarely disappoint me but this shit does.
-- oh really??? but all i see is some excitement.
-- emacs is an example of IDE.
-- so what the fuck is IDE anyway?
-- some ideas will be gathered from it, people who write programs every fucking day.
-- like photoshop. ideas of picture processing.
-- there must be some jobs for this machine to run.
-- wahtever. think about it. what matters the most?
-- sense? hearing?