#!/bin/bash
# start a language server?
mkfifo /tmp/lazero
# mkfifo /tmp/lazero_python
# no newline???
# timeout 2 cat /tmp/lazero &
# timeout 2 cat Main.py > /tmp/lazero_python &
# timeout 2 python3 /tmp/lazero_python > /tmp/lazero 
# ls -lth | awk '{print $1 " " $3}'
# xargs. and more.
# no we cannot share file content. it is use-after-free.
# cat > /tmp/lazero &
# echo $! > /tmp/
# it will be stucked.
# use the file like the same??
# read file content???
# multipipe???
# this will end once receive the file. but what about others??
# timeout is some kind of normalization.
# whatever. we need to wait, subscribe, timeout things??
# what is that dogtail thing?
# echo "this is the main lazero program."
# jshell can be great. however there is a huge misunderstanding here.
# what about conbining it with other snippets?
# use screen will do the job. but what about windows?
# check for detachable shell server???
# we need something like GUI, no abrupt change. something like sound, changing all the time????
# sense it, it is always streaming. creating streaming interactions.
# detachable complier, intepreter.....
# whatever.
# must follow next to each other.
# does this thing know what is constant?
# and what is dynamic?
# what is .jsh, jsx, all that kind of scripting language????
# cat main.lua | lua /dev/stdin
# how do we use pipes???
# ctrl-d.
# redirect the output, input file???
# what about different programs???
# sample=/tmp/lazero/sample.lua
# # echo $SAMPLE
# touch $sample
# cat main.lua > $sample
# lua $sample
# rm $sample