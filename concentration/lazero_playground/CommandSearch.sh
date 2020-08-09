#!/bin/bash
function command-search
{
   oldIFS=${IFS}
   IFS=":"

   for p in ${PATH}
   do
      ls $p | grep $1
   done

   export IFS=${oldIFS}
}
