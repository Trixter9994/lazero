#!/bin/bash
function command-grep
{
   oldIFS=${IFS}
   IFS=":"

   for p in ${PATH}
   do
      ls $p
   done

   export IFS=${oldIFS}
}

command-grep | cat > "CommandGrepMainIndex.txt"
